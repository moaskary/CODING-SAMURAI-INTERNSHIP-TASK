import requests

# set the target city
city = input("Enter city name: ")
# set the API key from open weather map
api_key = '204f1cd6ea07ab344596e234f48d0b2d'

# connect to URL 
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# run the URL
response = requests.get(url)

# if the request is successful 
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    print(f"Current weather in {city}: {weather}")
    print(f"The Temperature is : {temperature}°C")
    print(f"The humidity is {humidity}")
    print(f"Wind speed is : {wind}")
else:
    print(f"Failed to fetch weather data: {response.status_code}")
