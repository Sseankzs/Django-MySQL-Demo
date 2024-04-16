from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("menu/", views.menu, name="menu"),
    path("menu/functions/", views.functions, name="functions"),
    path("home/", views.home, name="home"),
    path("logout/", views.logout_user, name="logout"),
    path("swarms/", views.swarms, name="swarms"),
    path("details/<int:chompskis_id>/", views.details, name="details"),
    path("delete_chompski/<int:chompskis_id>/", views.delete_chompski, name="delete_chompski"),
    path("add_chompski/", views.add_chompski, name="add_chompski"),
    path("update_chompski/<int:chompskis_id>/", views.update_chompski, name="update_chompski"),
    path("swarm_details/<int:swarm_id>/", views.swarm_details, name="swarm_details"),
    path("home/sortbyname", views.chompski_sortby_name, name="chompski_sortby_name"),
    path("home/sortbyage", views.chompski_sortby_age, name="chompski_sortby_age"),
    path("home/sortbyheight", views.chompski_sortby_height, name="chompski_sortby_height"),
    path("home/sortbyweight", views.chompski_sortby_weight, name="chompski_sortby_weight"),
    path("home/sortbyteeth", views.chompski_sortby_teeth, name="chompski_sortby_teeth"),
    path("home/sortbyswarm", views.chompski_sortby_swarm, name="chompski_sortby_swarm"),
    path("swarm/sortbyname", views.swarm_sortby_name, name="swarm_sortby_name"),
    path("swarm/sortbyquantity", views.swarm_sortby_quantity, name="swarm_sortby_quantity"),
    path("swarm/sortbylatitude", views.swarm_sortby_latitude, name="swarm_sortby_latitude"),
    path("swarm/sortbylongitude", views.swarm_sortby_longitude, name="swarm_sortby_longitude"),
    path("delete_swarm/<int:swarm_id>/", views.delete_swarm, name="delete_swarm"),
    path("update_swarm/<int:swarm_id>/", views.update_swarm, name="update_swarm"),
    path("add_swarm/", views.add_swarm, name="add_swarm"),
    path("statistics/", views.statistics, name="statistics"),
]