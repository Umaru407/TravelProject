# Generated by Django 4.1.7 on 2023-05-16 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('a_Id', models.AutoField(primary_key=True, serialize=False)),
                ('m_Id', models.IntegerField()),
                ('a_Account', models.CharField(max_length=20, unique=True)),
                ('a_Password', models.CharField(max_length=20)),
                ('a_Level', models.IntegerField()),
                ('a_rank', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('f_Id', models.AutoField(primary_key=True, serialize=False)),
                ('f_Lang', models.CharField(max_length=10)),
                ('f_Name', models.CharField(max_length=50)),
                ('f_Summary', models.CharField(max_length=2000)),
                ('f_Introduction', models.TextField(max_length=1000)),
                ('f_OpenTime', models.CharField(max_length=2000)),
                ('f_District', models.CharField(max_length=50)),
                ('f_Address', models.CharField(max_length=100)),
                ('f_Tel', models.CharField(max_length=20)),
                ('f_Fax', models.CharField(max_length=50)),
                ('f_Latitude', models.FloatField(max_length=10)),
                ('f_Longtitude', models.FloatField(max_length=10)),
                ('f_Services', models.CharField(max_length=100)),
                ('f_Category', models.CharField(max_length=100)),
                ('f_Consume', models.CharField(max_length=20)),
                ('f_UpdateTime', models.CharField(max_length=50)),
                ('f_Stars', models.FloatField(default=None, max_length=10, null=True)),
                ('f_Reviews', models.IntegerField(default=None, null=True)),
                ('f_Likes', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('h_Id', models.AutoField(primary_key=True, serialize=False)),
                ('h_Name', models.CharField(max_length=50)),
                ('h_Summary', models.CharField(max_length=2000, null=True)),
                ('h_Introduction', models.TextField(max_length=400, null=True)),
                ('h_OpenTime', models.CharField(max_length=2000, null=True)),
                ('h_District', models.CharField(max_length=50, null=True)),
                ('h_Address', models.CharField(max_length=100)),
                ('h_Tel', models.CharField(max_length=20, null=True)),
                ('h_Fax', models.CharField(max_length=50, null=True)),
                ('h_Latitude', models.FloatField(max_length=10)),
                ('h_Longtitude', models.FloatField(max_length=10)),
                ('h_Services', models.CharField(max_length=100, null=True)),
                ('h_Category', models.CharField(max_length=100)),
                ('h_UpdateTime', models.CharField(max_length=50)),
                ('h_Stars', models.FloatField(default=None, max_length=10, null=True)),
                ('h_Reviews', models.IntegerField(default=None, null=True)),
                ('h_Likes', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('m_Id', models.AutoField(primary_key=True, serialize=False)),
                ('m_Name', models.CharField(max_length=10, unique=True)),
                ('m_Gender', models.CharField(default='m', max_length=2)),
                ('m_Old', models.IntegerField()),
                ('m_Email', models.EmailField(blank=True, default='', max_length=100)),
                ('m_Phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('s_Id', models.AutoField(primary_key=True, serialize=False)),
                ('s_Lang', models.CharField(max_length=10)),
                ('s_Name', models.CharField(max_length=50)),
                ('s_Summary', models.CharField(max_length=2000)),
                ('s_Introduction', models.TextField(max_length=2000)),
                ('s_OpenTime', models.CharField(max_length=2000)),
                ('s_District', models.CharField(max_length=50)),
                ('s_Address', models.CharField(max_length=100)),
                ('s_Tel', models.CharField(max_length=50)),
                ('s_Fax', models.CharField(max_length=50)),
                ('s_Latitude', models.FloatField(max_length=10)),
                ('s_Longtitude', models.FloatField(max_length=10)),
                ('s_Services', models.CharField(max_length=100)),
                ('s_Category', models.CharField(max_length=100)),
                ('s_UpdateTime', models.CharField(max_length=50)),
                ('s_Stars', models.FloatField(default=None, max_length=10, null=True)),
                ('s_Reviews', models.IntegerField(default=None, null=True)),
                ('s_Likes', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Travel_List',
            fields=[
                ('t_Id', models.AutoField(primary_key=True, serialize=False)),
                ('m_Id', models.IntegerField()),
                ('t_Name', models.CharField(max_length=10)),
                ('t_Description', models.CharField(max_length=10)),
                ('t_FormTime', models.DateTimeField(auto_now=True)),
                ('t_StartDate', models.CharField(max_length=100)),
                ('t_EndDate', models.CharField(max_length=100)),
                ('t_StayDay', models.IntegerField(default='1')),
                ('t_Privacy', models.CharField(default='n', max_length=2)),
                ('t_Views', models.IntegerField()),
                ('t_Likes', models.IntegerField()),
                ('t_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Travel_List_Detail',
            fields=[
                ('tl_Id', models.AutoField(primary_key=True, serialize=False)),
                ('tl_TransportMode', models.CharField(max_length=20)),
                ('tl_TransportTime', models.IntegerField()),
                ('tl_StartTime', models.CharField(default='08:00', max_length=10)),
                ('tl_StayTime', models.IntegerField(default=2, max_length=10)),
                ('tl_Day', models.IntegerField(default=1)),
                ('tl_Order', models.IntegerField()),
                ('tl_Notes', models.CharField(max_length=200)),
                ('tl_score', models.IntegerField(default=0)),
                ('f_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.food')),
                ('h_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.hotel')),
                ('s_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.spot')),
                ('t_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.travel_list')),
            ],
        ),
        migrations.CreateModel(
            name='s_Picture',
            fields=[
                ('sp_Id', models.AutoField(primary_key=True, serialize=False)),
                ('sp_URL', models.ImageField(default=None, upload_to='images/spot/')),
                ('s_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.spot')),
            ],
        ),
        migrations.CreateModel(
            name='s_Interest',
            fields=[
                ('si_Id', models.AutoField(primary_key=True, serialize=False)),
                ('si_pg', models.IntegerField()),
                ('si_os', models.IntegerField()),
                ('si_tp', models.IntegerField()),
                ('si_ee', models.IntegerField()),
                ('si_ff', models.IntegerField()),
                ('si_la', models.IntegerField()),
                ('si_le', models.IntegerField()),
                ('si_ns', models.IntegerField()),
                ('si_np', models.IntegerField()),
                ('si_rt', models.IntegerField()),
                ('si_se', models.IntegerField()),
                ('si_ha', models.IntegerField()),
                ('si_tf', models.IntegerField()),
                ('m_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.member')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('q_Id', models.AutoField(primary_key=True, serialize=False)),
                ('q_question', models.CharField(default=None, max_length=100)),
                ('q_answer', models.CharField(default=None, max_length=100)),
                ('q_type', models.CharField(default=None, max_length=50)),
                ('q_solution', models.CharField(default=None, max_length=100)),
                ('q_right', models.IntegerField(default=0)),
                ('q_false', models.IntegerField(default=0)),
                ('s_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.spot')),
            ],
        ),
        migrations.CreateModel(
            name='m_Picture',
            fields=[
                ('mp_Id', models.AutoField(primary_key=True, serialize=False)),
                ('mp_URL', models.ImageField(default=None, upload_to='images/member/')),
                ('m_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.member')),
            ],
        ),
        migrations.CreateModel(
            name='Like_Record',
            fields=[
                ('r_Id', models.AutoField(primary_key=True, serialize=False)),
                ('r_LikeOrDisLike', models.IntegerField(default=0)),
                ('f_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.food')),
                ('h_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.hotel')),
                ('m_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.member')),
                ('s_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.spot')),
                ('t_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.travel_list')),
            ],
        ),
        migrations.CreateModel(
            name='h_Picture',
            fields=[
                ('hp_Id', models.AutoField(primary_key=True, serialize=False)),
                ('hp_URL', models.ImageField(default=None, upload_to='images/hotel/')),
                ('h_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='f_Picture',
            fields=[
                ('fp_Id', models.AutoField(primary_key=True, serialize=False)),
                ('fp_URL', models.ImageField(default=None, upload_to='images/food /')),
                ('f_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.food')),
            ],
        ),
    ]
