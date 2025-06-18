import requests

API_KEY = "6458211682c38baff1ea1302aa74a600"  # kendi API anahtarın
GEOCODING_URL = "http://api.openweathermap.org/geo/1.0/direct"
ONECALL_URL = "https://api.openweathermap.org/data/3.0/onecall"

def get_weather_data(city):
    geo_params = {
        "q": city,
        "limit": 1,
        "appid": API_KEY
    }
    geo_response = requests.get(GEOCODING_URL, params=geo_params)
    if geo_response.status_code != 200 or not geo_response.json():
        print("Şehir bulunamadı.")
        return None

    location = geo_response.json()[0]
    lat = location["lat"]
    lon = location["lon"]

    weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",
        "lang": "tr"
    }
    response = requests.get(ONECALL_URL, params=weather_params)
    if response.status_code == 200:
        data = response.json()
        current = data["current"]
        result = {
            "city": city.title(),
            "temperature": current["temp"],
            "description": current["weather"][0]["description"],
            "humidity": current["humidity"],
            "icon": current["weather"][0]["icon"]
        }
        return result
    else:
        print("API'den veri alınamadı.")
        return None
