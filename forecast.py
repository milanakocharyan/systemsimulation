import requests
import json

def get_weather(city_name):
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = 'YOUR_API_KEY'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # You can change units to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                'City': data['name'],
                'Temperature (°C)': data['main']['temp'],
                'Description': data['weather'][0]['description'],
                'Humidity (%)': data['main']['humidity'],
                'Wind Speed (m/s)': data['wind']['speed']
            }

            return weather_info
        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    print("Welcome to the Weather Forecast App!")

    while True:
        city_name = input("Enter the city name (or 'quit' to exit): ")

        if city_name.lower() == 'quit':
            print("Exiting the Weather Forecast App. Goodbye!")
            break

        weather_info = get_weather(city_name)

        if weather_info:
            print("\nWeather Forecast:")
            for key, value in weather_info.items():
                print(f"{key}: {value}")

if __name__ == "__main__":
    main()
