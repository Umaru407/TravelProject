from ..models import  Account, Spot
from ..serializers import SpotSerializer
from django.http import JsonResponse

def get_spot_json():
    spots = Spot.objects.all().order_by('-s_Id')
    serializer = SpotSerializer(spots, many=True)
    spot_json = serializer.data

    # 可以对 spot_json 进行进一步处理或返回
    return spot_json

spot_json = get_spot_json()
print(spot_json)