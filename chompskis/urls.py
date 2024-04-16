from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("menu/", views.menu, name="menu"),
    path("menu/functions/", views.functions, name="functions"),
    path("home/", views.home, name="home"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("swarms/", views.swarms, name="swarms"),
    path("details/<int:chompskis_id>/", views.details, name="details"),
    path("delete_chompski/<int:chompskis_id>/", views.delete_chompski, name="delete_chompski"),
    path("add_chompski/", views.add_chompski, name="add_chompski"),
]