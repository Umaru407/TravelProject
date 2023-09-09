# Generated by Django 4.1.7 on 2023-09-08 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("account", models.CharField(max_length=20, unique=True)),
                ("email", models.EmailField(default="", max_length=254, unique=True)),
                ("username", models.CharField(default="", max_length=100)),
                ("rank", models.IntegerField(default=0)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Food",
            fields=[
                ("f_Id", models.AutoField(primary_key=True, serialize=False)),
                ("f_Lang", models.CharField(max_length=10)),
                ("f_Name", models.CharField(max_length=50)),
                ("f_Summary", models.CharField(max_length=2000)),
                ("f_Introduction", models.TextField(max_length=1000)),
                ("f_OpenTime", models.CharField(max_length=2000)),
                ("f_District", models.CharField(max_length=50)),
                ("f_Address", models.CharField(max_length=100)),
                ("f_Tel", models.CharField(max_length=20)),
                ("f_Fax", models.CharField(max_length=50)),
                ("f_Latitude", models.FloatField(max_length=10)),
                ("f_Longitude", models.FloatField(max_length=10)),
                ("f_Services", models.CharField(max_length=100)),
                ("f_Category", models.CharField(max_length=100)),
                ("f_Consume", models.CharField(max_length=20)),
                ("f_UpdateTime", models.CharField(max_length=50)),
                ("f_Stars", models.FloatField(default=None, max_length=10, null=True)),
                ("f_Reviews", models.IntegerField(default=None, null=True)),
                ("f_Likes", models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Hotel",
            fields=[
                ("h_Id", models.AutoField(primary_key=True, serialize=False)),
                ("h_Name", models.CharField(max_length=50)),
                ("h_Summary", models.CharField(max_length=2000, null=True)),
                ("h_Introduction", models.TextField(max_length=400, null=True)),
                ("h_OpenTime", models.CharField(max_length=2000, null=True)),
                ("h_District", models.CharField(max_length=50, null=True)),
                ("h_Address", models.CharField(max_length=100)),
                ("h_Tel", models.CharField(max_length=20, null=True)),
                ("h_Fax", models.CharField(max_length=50, null=True)),
                ("h_Latitude", models.FloatField(max_length=10)),
                ("h_Longitude", models.FloatField(max_length=10)),
                ("h_Services", models.CharField(max_length=100, null=True)),
                ("h_Category", models.CharField(max_length=100)),
                ("h_UpdateTime", models.CharField(max_length=50)),
                ("h_Stars", models.FloatField(default=None, max_length=10, null=True)),
                ("h_Reviews", models.IntegerField(default=None, null=True)),
                ("h_Likes", models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Spot",
            fields=[
                ("s_Id", models.AutoField(primary_key=True, serialize=False)),
                ("s_Lang", models.CharField(max_length=10)),
                ("s_Name", models.CharField(max_length=50)),
                ("s_Summary", models.CharField(max_length=2000)),
                ("s_Introduction", models.TextField(max_length=2000)),
                ("s_OpenTime", models.CharField(max_length=2000)),
                ("s_District", models.CharField(max_length=50)),
                ("s_Address", models.CharField(max_length=100)),
                ("s_Tel", models.CharField(max_length=50)),
                ("s_Fax", models.CharField(max_length=50)),
                ("s_Latitude", models.FloatField(max_length=10)),
                ("s_Longitude", models.FloatField(max_length=10)),
                ("s_Services", models.CharField(max_length=100)),
                ("s_Category", models.CharField(max_length=100)),
                ("s_UpdateTime", models.CharField(max_length=50)),
                ("s_Stars", models.FloatField(default=None, max_length=10, null=True)),
                ("s_Reviews", models.IntegerField(default=None, null=True)),
                ("s_Likes", models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Travel_List",
            fields=[
                ("t_Id", models.AutoField(primary_key=True, serialize=False)),
                ("t_Name", models.CharField(max_length=10)),
                ("t_Description", models.CharField(max_length=10)),
                ("t_FormTime", models.DateTimeField(auto_now=True)),
                ("t_StartDate", models.CharField(max_length=100)),
                ("t_EndDate", models.CharField(max_length=100)),
                ("t_StayDay", models.IntegerField(default=1)),
                ("t_Privacy", models.CharField(default="n", max_length=2)),
                ("t_Views", models.IntegerField()),
                ("t_Likes", models.IntegerField()),
                ("t_score", models.IntegerField(default=0)),
                (
                    "account",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Travel_List_StartTime",
            fields=[
                ("tls_Id", models.AutoField(primary_key=True, serialize=False)),
                ("tls_Day", models.IntegerField(default=1)),
                ("tls_StartTime", models.IntegerField(default=28800)),
                (
                    "t_Id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.travel_list",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Travel_List_Detail",
            fields=[
                ("tl_Id", models.AutoField(primary_key=True, serialize=False)),
                ("tl_TransportMode", models.CharField(max_length=20, null=True)),
                ("tl_TransportTime", models.IntegerField(null=True)),
                ("tl_StayTime", models.IntegerField(default=2, max_length=10)),
                ("tl_Day", models.IntegerField(default=1)),
                ("tl_Order", models.IntegerField()),
                ("tl_Notes", models.CharField(max_length=200, null=True)),
                ("tl_score", models.IntegerField(default=0)),
                (
                    "f_Id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.food",
                    ),
                ),
                (
                    "h_Id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.hotel",
                    ),
                ),
                (
                    "s_Id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.spot",
                    ),
                ),
                (
                    "t_Id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.travel_list",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="s_Picture",
            fields=[
                ("sp_Id", models.AutoField(primary_key=True, serialize=False)),
                ("sp_URL", models.ImageField(default=None, upload_to="images/spot/")),
                (
                    "s_Id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.spot"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="s_Interest",
            fields=[
                ("si_Id", models.AutoField(primary_key=True, serialize=False)),
                ("si_hv", models.IntegerField()),
                ("si_sa", models.IntegerField()),
                ("si_os", models.IntegerField()),
                ("si_la", models.IntegerField()),
                ("si_mf", models.IntegerField()),
                ("si_ee", models.IntegerField()),
                ("si_ns", models.IntegerField()),
                ("si_ff", models.IntegerField()),
                ("si_pg", models.IntegerField()),
                ("si_tf", models.IntegerField()),
                ("si_pd", models.IntegerField()),
                ("si_ha", models.IntegerField()),
                ("si_np", models.IntegerField()),
                ("si_tp", models.IntegerField()),
                ("si_se", models.IntegerField()),
                ("si_rt", models.IntegerField()),
                ("si_lb", models.IntegerField()),
                ("si_le", models.IntegerField()),
                (
                    "id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("q_Id", models.AutoField(primary_key=True, serialize=False)),
                ("q_question", models.CharField(default=None, max_length=100)),
                ("q_answer", models.CharField(default=None, max_length=100)),
                ("q_type", models.CharField(default=None, max_length=50)),
                ("q_solution", models.CharField(default=None, max_length=100)),
                ("q_right", models.IntegerField(default=0)),
                ("q_false", models.IntegerField(default=0)),
                (
                    "s_Id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.spot"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Like_Record",
            fields=[
                ("r_Id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "f_Id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.food",
                    ),
                ),
                (
                    "h_Id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.hotel",
                    ),
                ),
                (
                    "id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "s_Id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.spot",
                    ),
                ),
                (
                    "t_Id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.travel_list",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="h_Picture",
            fields=[
                ("hp_Id", models.AutoField(primary_key=True, serialize=False)),
                ("hp_URL", models.ImageField(default=None, upload_to="images/hotel/")),
                (
                    "h_Id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.hotel"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="f_Picture",
            fields=[
                ("fp_Id", models.AutoField(primary_key=True, serialize=False)),
                ("fp_URL", models.ImageField(default=None, upload_to="images/food /")),
                (
                    "f_Id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.food"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="a_Picture",
            fields=[
                ("ap_Id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "ap_URL",
                    models.ImageField(default=None, upload_to="images/account/"),
                ),
                (
                    "id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
