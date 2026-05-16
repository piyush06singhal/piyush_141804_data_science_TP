import pandas as pd
import requests
def get_current_weather(api_key, city_name):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric",
    }

    response = requests.get(url, params=params, timeout=10)
    data = response.json()

    if response.status_code != 200:
        message = data.get("message", "Unable to fetch weather data")
        raise Exception(message)

    weather_data = {
        "City": data["name"],
        "Country": data["sys"]["country"],
        "Temperature (C)": data["main"]["temp"],
        "Feels Like (C)": data["main"]["feels_like"],
        "Weather": data["weather"][0]["description"],
        "Humidity (%)": data["main"]["humidity"],
    }
    return weather_data

def main():
    api_key = "bd5e378503939ddaee76f12ad7a97608"
    city_name = input("Enter city name: ").strip()

    try:
        weather_data = get_current_weather(api_key, city_name)
        df = pd.DataFrame([weather_data])
        print("\nCurrent Weather Details:")
        print(df.to_string(index=False))
        print(f"\nExact current temperature in {weather_data['City']}: {weather_data['Temperature (C)']} C")
        
    except Exception as error:
        print(f"Error: {error}")

main()
