from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.weather, name="weather"),
    path("get_weather", views.get_weather, name="get_weather"),
]
