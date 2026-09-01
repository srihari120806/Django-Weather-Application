import requests
from django.conf import settings
from django.shortcuts import render

def index(request):
    context = {}
    if request.method == "POST":
        city = request.POST.get("city", "").strip()
        if not city:
            context["error"] = "Please enter a city name."
        elif not settings.OPENWEATHER_API_KEY:
            context["error"] = "OpenWeather API key is not configured."
        else:
            try:
                response = requests.get(
                    "https://api.openweathermap.org/data/2.5/weather",
                    params={"q": city, "appid": settings.OPENWEATHER_API_KEY, "units": "metric"},
                    timeout=10,
                )
                data = response.json()
                if response.status_code == 200:
                    context["weather"] = {
                        "city": data["name"],
                        "country": data["sys"]["country"],
                        "temperature": round(data["main"]["temp"]),
                        "feels_like": round(data["main"]["feels_like"]),
                        "humidity": data["main"]["humidity"],
                        "wind_speed": data.get("wind", {}).get("speed", 0),
                        "description": data["weather"][0]["description"].title(),
                        "icon": data["weather"][0]["icon"],
                    }
                else:
                    context["error"] = data.get("message", "City not found. Please try again.")
            except requests.RequestException:
                context["error"] = "Unable to connect to the weather service. Please try again."
    return render(request, "weather/index.html", context)
