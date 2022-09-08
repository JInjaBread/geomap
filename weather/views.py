import http, json
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def weather_update(lat, lng):
    conn = http.client.HTTPSConnection("api.openweathermap.org")
    authkey = settings.AUTH_KEY
    headers = { 'content-type': "application/json" }
    url = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lng+"&appid="+authkey
    conn.request("GET", url , headers=headers)
    res = conn.getresponse()
    data = res.read()
    return data

def weather(request):

    return render(request, 'weather/index.html')

@csrf_exempt
def get_weather(request):
    if request.method != 'POST':
        return HttpResponse("Invalid Method")
    elif request.method == 'POST':
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        try:
            data = weather_update(lat, lng)
            return HttpResponse(data)
        except Exception as e:
            return HttpResponse(e)
