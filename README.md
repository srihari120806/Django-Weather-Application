# 🌤️ Django Weather Application

A simple Django-based weather application that lets users search for a city and view current weather information using the OpenWeather API.

## Features
- City-based weather search
- Current temperature
- Feels-like temperature
- Humidity
- Wind speed
- Weather description and icon
- Error handling for invalid searches and API connection issues

## Technologies
- Python
- Django
- Requests
- OpenWeather API
- HTML & CSS

## Project Structure
```text
Django-Weather-Application/
├── manage.py
├── requirements.txt
├── weather_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── weather/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    └── templates/
        └── weather/
            └── index.html
```

## Setup
```bash
python -m venv venv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Set your `OPENWEATHER_API_KEY` environment variable before running the application.

## Author
M. Srihari
