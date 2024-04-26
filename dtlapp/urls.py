from django.urls import path

from dtlapp import views

urlpatterns = [
    path("make", views.home),
]
