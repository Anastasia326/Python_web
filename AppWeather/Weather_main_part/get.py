import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def get_something(url, form):
    cities = City.objects.all()[::-1]

    all_cities = []

    for city in cities:
        try:
            res = requests.get(url.format(city.name)).json()
            city_info = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'humidity': res["main"]["humidity"],
                'icon': res["weather"][0]["icon"]
            }

            all_cities.append(city_info)
        except:
            pass

    context = {'all_info': all_cities, 'form': form, 'now_value': all_cities[0], 'size': len(all_cities)}
    return context
