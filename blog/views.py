from django.shortcuts import render
import json
import os
import requests
import json


def home(request):
    return render(request, 'blog/index.html')


api_key = 'a2a1bd77a538412180c53038231106'
os.chdir(os.getcwd() + "/blog")
def weather(request):
    city = request.GET.get('city')
    api_key = 'a2a1bd77a538412180c53038231106'
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=7'
    response = requests.get(url)
    data = json.loads(response.text)
    if response.status_code == 200:
        forecast = data['forecast']['forecastday']
        context = {
            'city': city,
            'forecast': [
                {
                    'date': day['date'],
                    'condition': day['day']['condition']['text'],
                    'max_temp': day['day']['maxtemp_c'],
                    'min_temp': day['day']['mintemp_c'],
                    'weather_icon': day['day']['condition']['icon']
                }
                for day in forecast
            ]
        }
        return render(request, 'blog/weather.html', context=context)
    else:
        return render(request, 'blog/error.html', context={
            'error' : "Mavjud bolmagan davlatni kiritingiz "
        })

    # return render(request, 'blog/weather.html')