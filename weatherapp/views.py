from django.shortcuts import render,redirect
from .models import City
from django.contrib import messages
import requests



def homepage(request):

    if request.method=='POST':
        cityname = request.POST.get('city')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={cityname}&units=imperial&appid=31416401e150b03ebefd41187a5a4554'
        try:
            city_data = requests.get(url).json()
            City.objects.get_or_create(name=cityname,description=city_data['weather'][0]['main'],icon=city_data['weather'][0]['icon'],temprature=city_data['main']['temp'])
            messages.success(request,('City has been added'))
        except :
            messages.success(request,('Unable to add city'))

    db_weather = City.objects.order_by('name')
    weather_dict = {'weather_data':db_weather}
    return render(request,'homepage.html',weather_dict)


def delete_weather(request,id):
    deletable = City.objects.get(id=id)
    deletable.delete()
    messages.success(request,(f'{deletable} Has been deleted'))
    return redirect('/')




