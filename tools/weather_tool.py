import requests

CITY_COORDS = {
    "bangalore": (12.97, 77.59),
    "delhi": (28.61, 77.21),
    "mumbai": (19.07, 72.87),
    "chennai": (13.08, 80.27),
    "kolkata": (22.57, 88.36)
}

def get_weather(city: str):
    city_key = city.lower()

    if city_key not in CITY_COORDS:
        return {"error": "City not supported"}

    lat, lon = CITY_COORDS[city_key]

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current_weather=true"
    )

    response = requests.get(url, timeout=10)
    data = response.json().get("current_weather", {})

    return {
        "city": city.title(),
        "temperature_c": data.get("temperature"),
        "windspeed_kmh": data.get("windspeed"),
        "weathercode": data.get("weathercode")
    }
