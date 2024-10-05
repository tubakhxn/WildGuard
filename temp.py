import requests

def get_weather(city):
    API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key from openweathermap.org
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"City: {city}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
    else:
        print("City not found. Please try again.")

if __name__ == "__main__":
    city = input("Enter the name of a city: ")
    get_weather(city)
