from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("menu/", views.menu, name="menu"),
    path("menu/functions/", views.functions, name="functions"),
    path("home/", views.home, name="home"),
    path("logout/", views.logout_user, name="logout")
]