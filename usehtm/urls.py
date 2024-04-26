from django.urls import path

from usehtm import views

urlpatterns = [
    path("home/",views.home),
    path("about/",views.about),
    path("role/",views.role),
    path("home1/",views.home1),
    ]