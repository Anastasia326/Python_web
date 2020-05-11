import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from .get import get_something

def index(request):
    appid = '60762f39833d5027ecddd7ce126a7ee6'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        print(request.POST)
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    context = get_something(url, form)

    return render(request, 'weather_/index.html', context)
