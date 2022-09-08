from django.test import TestCase
from django.urls import reverse, resolve
from .views import weather, weather_update
# Create your tests here.

class BasicTest(TestCase):
    def test_url_index(self):
        url = reverse('weather')
        print(resolve(url))

    def test_function_weather_update(self):
        f = weather_update(str(13.1391), str(123.7438))
        print(f)
