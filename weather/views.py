import requests
from django.shortcuts import render

def index(request):
    return render(request, 'weather/index.html', {'title': 'My Weather App'})

def weather(request):

    if request.method == "POST":
        city_name = request.POST['cityname']

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f40144229c726bb67506050da3602379'
    city = city_name
    
    try:
        req = requests.get(url.format(city)).json()
        
        city_weather_details = {
            'City': city,
            'Temperature': req['main']['temp'],
            'Description': req['weather'][0]['description'],
            'Pressure': req['main']['pressure'],
            'Humidity': req['main']['humidity'],
            'Country': req['sys']['country'],
            'Icon': req['weather'][0]['icon']
        }
        context = {
        'city_weather': city_weather_details
    }
    except KeyError:
        return render(request, 'weather/pagenotfound.html')
   
    return render(request, 'weather/weather.html', context)