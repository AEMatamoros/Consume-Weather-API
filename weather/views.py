from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    url= "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=946d6016f64416612727def0f27e3064"
    city_data= {}
    city=""
    if request.method == 'POST':
        city= (request.POST.get("search_city"))
    if (city !=""):
        r = requests.get(url.format(city)).json()
    
        city_data = {"city":city,
                "temperature": round((((r["main"]["temp"])-32)/1.8),2),
                "description": r["weather"][0]["description"],
                "icon": r["weather"][0]["icon"],}

    context={"city_data":city_data}
    return render(request,'weather/main.html',context);