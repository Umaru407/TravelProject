from ..models import Spot
from ..serializers import SpotSerializer
from django.http import JsonResponse
from ..utils import method
from ..utils import Byinterest #import interest_pick
from ..utils import Bypopular #import popular_pick
from ..utils import Byschedule
from ..utils import travel_list_detail_data
import json
#interest_data = {}
# playzone_data={}
# custom = True

# def get_t_Id(data):
#     t_Id=data
#     print(t_Id)

# def process_interest_data(data):
#     global interest_data
#     interest_data = data
#     for key, value in interest_data.items():
#         print(f"Interest {key}: {value}")

# def process_playzone_data(data):
#     global playzone_data
#     playzone_data = data
#     for zone in playzone_data:
#         print("Playzone:", zone)
#     print(custom)

# def spotList():
#     spots = Spot.objects.all().order_by('-s_Id')
#     serializer = SpotSerializer(spots, many=True)
#     return JsonResponse(serializer.data, safe=False)

# def spotListid(s_id):
#     spot=ai_test.get_spot_json(s_id)
#     return spot


# 李誌軒

class main():
    #play = main(t_id, user_id, interest_list, play_zone)    
    def __init__(self, t_id, interest_list, play_zone, benchmark_pos) -> None:

        self.spot_json, self.spots_name, self.topic_matrix= method.get_spot_json(play_zone)

        self.t_id = t_id

        self.playtime, self.user_id= method.get_tl_INFO(t_id)

        self.user_interest = method.get_interest_json(self.user_id, interest_list) 

        print(self.user_interest)
        
        self.interest_pick_method = Byinterest.interest_pick(self.user_interest, self.spots_name, self.topic_matrix)
        self.popular_pick_method = Bypopular.popular_pick(self.spot_json, self.spots_name)
        self.Schedule = Byschedule.schedule()

        self.playtime_day = list(self.playtime.keys())
        self.playtime_hours = [int(x / 2 + 1) for x in list(self.playtime.values())]
        self.play_zone = play_zone
        self.benchmark_pos = benchmark_pos

    def recom_spot(self, n, havebeen2):

        #interest matrix pick  
        interest_pick = self.interest_pick_method.pick(60)

        # classification
        classification = None

        top_n = n
        #popular pick
        popular_pick, popular_id = self.popular_pick_method.pick(interest_pick, top_n, classification, havebeen2)

        return popular_pick, popular_id
    
    def spot_schedule(self, topspotid, playtime):
        morning_only_spots, afternoon_only_spots, allday_opening_spots = self.Schedule.bytime(topspotid, playtime)
        morn_sorted_locations, other_sorted_locations, afternoon_sorted_locations = self.Schedule.byposition(morning_only_spots, afternoon_only_spots, allday_opening_spots, self.benchmark_pos)
        # if morn_sorted_locations != None:
        #     if afternoon_sorted_locations != None:
                
        return [item for sublist in [morn_sorted_locations, other_sorted_locations, afternoon_sorted_locations] if sublist is not None for item in sublist]
    
    def recom_food(self, scheduled_spot_id):
        first_spot = scheduled_spot_id[0]
        second_spot = scheduled_spot_id[1]
        last_spot = scheduled_spot_id[-1]

        all_food = [food["f_Id"] for food in self.food_json]
        all_food_position = [method.getfoodbyid(-food, "position") for food in all_food][::-1]

        breakfast = self.Schedule.food(method.getspotbyid(-first_spot, "position"), all_food_position)
        lunch = self.Schedule.food(method.getspotbyid(-second_spot, "position"), all_food_position)
        dinner = self.Schedule.food(method.getspotbyid(-last_spot, "position"), all_food_position)

        for j, i in zip([breakfast, lunch, dinner], [0, 2+1, len(scheduled_spot_id)+2]):
            scheduled_spot_id = scheduled_spot_id[:i] + [j] + scheduled_spot_id[i:]

        return scheduled_spot_id
    
    def recom_hotel(self, sorted_location):
        
        last_spot_id = sorted_location[-2]
        last_spot_position = method.getspotbyid(-last_spot_id, "position")
    
        all_hotel = [hotel["h_Id"] for hotel in self.hotel_json]
        all_hotel_position = [method.gethotelbyid(-hotel, "position") for hotel in all_hotel][::-1]

        recom_hotel_id = self.Schedule.hotel(last_spot_position, all_hotel_position)
        
        return recom_hotel_id, [method.gethotelbyid(-id, "h_Name") for id in recom_hotel_id]
    
    def schedule_list(self, havebeen2 = []):    
        schedule_dic = []
        for i in range(len(self.playtime_day)):
            popular_pick, popular_id = self.recom_spot(self.playtime_hours[i], havebeen2)
            sc = self.spot_schedule(popular_id, [self.playtime_day[i]])
            #sc = self.recom_food(sc)
            #recom_hotel_id , recom_hotel = self.recom_hotel(sc)
            recom_hotel_id = None
            #schedule_dic[str(i)] = sc
            for j in range(len(sc)):
                aspot = {}
                aspot["t_id"] = self.t_id
                aspot["s_id"] = sc[j]
                if j == 0:
                    aspot['tl_TransportTime'] = 0
                else:
                    aspot['tl_TransportTime'] = method.transporttime(sc[j-1], sc[j])
                aspot['tl_Day'] = i
                schedule_dic.append(aspot)
            havebeen2 += popular_id
        
        schedule_dic = json.dumps(schedule_dic, indent=4)
        # print(schedule_dic)
        travel_list_detail_data.travel_list_detail_data_add(schedule_dic)
        return "done"

#Data
t_id = 1
start_location = (22.9908, 120.2033)

play_zone = ["北門區", "七股區", "鹽水區"]

interest_list = None

schedule_dic = main(t_id, interest_list, play_zone, start_location).schedule_list() # input:  t_id: travel list id
                                                                                            # interest_list 這是客製化才有的
                                                                                            # playzone: list of zones
                                                                                            # start_location: 
# print(schedule_dic)