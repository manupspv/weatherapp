from django.shortcuts import render
from django.http import JsonResponse
import json, requests



def home(request):


    if request.method == "POST":

        city = request.POST.get('city')
        req1 = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3b5ba28eb5798c2ea118328b073ec8bd')

        if req1.status_code == 404 or req1.status_code == 400:
            req1 = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Kozhikode&appid=3b5ba28eb5798c2ea118328b073ec8bd')
            req2 = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=11.25&lon=75.77&appid=3b5ba28eb5798c2ea118328b073ec8bd')

            weather_data1 = req1.json()
            weather_data2 = req2.json()

            context = {
                
                'error':True,
                'w1':weather_data1,
                'w2':weather_data2
            }
        else:
            weather_data1 = req1.json()
            lat = weather_data1['coord']['lat']
            lon = weather_data1['coord']['lon']
            
            req2 = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid=3b5ba28eb5798c2ea118328b073ec8bd')
            weather_data2 = req2.json()

            context = {

                'w1':weather_data1,
                'w2':weather_data2

            }
    else:

        req1 = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Kozhikode&appid=3b5ba28eb5798c2ea118328b073ec8bd')
        req2 = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=11.25&lon=75.77&appid=3b5ba28eb5798c2ea118328b073ec8bd')
        
        weather_data1 = req1.json()
        weather_data2 = req2.json()

        context = {

                'w1':weather_data1,
                'w2':weather_data2

        }


    return render(request, "weather_app/index.html", context)




def api(request):

    return render(request, "weather_app/index.html")

def contact(request):

    return render(request, "weather_app/index.html")