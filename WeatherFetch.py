import requests

API_KEY = "6900bf74553b4ebc45f4c2efe155e7f1"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=imperial"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description'].capitalize()
    temperature = round(data["main"]["temp"])
    feelsLike = round(data["main"]["feels_like"])
    dailyLow = data["main"]["temp_min"]
    dailyHigh = data["main"]["temp_max"]

    print()
    print(f"The city of {city} reports as follows:")
    print("Weather:", weather)
    print("Current temperature:", temperature, "farenheit")
    print("Feels like:", feelsLike, "farenheit")
    print()
    print("Todays low:", dailyLow, "farenheit")
    print("Todays high:", dailyHigh, "farenheit")

else:
    print("An error occurred.")