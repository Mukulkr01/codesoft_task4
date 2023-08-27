import requests

API_KEY = 'YOUR_API_KEY'  # Replace this with your actual API key
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_data(location):
    params = {
        'q': location,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None

def display_weather(data):
    if data is None:
        return

    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']

    print("Weather Forecast:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Description: {description.capitalize()}")

def main():
    print("Welcome to the Weather Forecast Application")
    location = input("Enter city name or zip code: ")
    
    weather_data = get_weather_data(location)
    display_weather(weather_data)

if __name__ == '__main__':
    main()
