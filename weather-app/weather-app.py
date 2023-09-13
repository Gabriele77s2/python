import requests

api_key = "YOUR_API_KEY"  # Replace with your actual API key
city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    print(f"Current temperature in {city}: {temperature}°C")
    print(f"Weather: {weather}")
else:
    print("Error fetching weather information")
