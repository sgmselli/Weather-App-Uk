import requests
import numpy

def latlng(location):
    API_KEY="googleMapsApiKey"
    BASE_URL="https://maps.googleapis.com/maps/api/geocode/json"

    request_url = f"{BASE_URL}?address=high+st+{location}&components=country:GB&key={API_KEY}"

    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        lat = data['results'][0]['geometry']['bounds']['northeast']['lat']
        lng = data['results'][0]['geometry']['bounds']['northeast']['lng']
        lArray = [lat, lng]
        return lArray
    else:
        return "An error occured"

def weather(lat, lng, location):
    API_KEY = "openWeatherMapApiKey"
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    request_url = f"{BASE_URL}?appid={API_KEY}&lat={lat}&lon={lng}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        print("The weather today in "+location+" is "+weather)
        temperature = numpy.round(data['main']['temp'] - 273.15, 0)
        print("The average temperature today in "+location+" is ",temperature,"°C")

        
        temperatureMin = numpy.round(data['main']['temp_min'] - 273.15, 0)
        print("The minimum temperature today in "+location+" is ",temperatureMin,"°C")

        
        temperatureMax = numpy.round(data['main']['temp_max'] - 273.15, 0)
        print("The maximum temperature today in "+location+" is ",temperatureMax,"°C")
    else:
        "An error occured"

location = input("Enter a UK location: ")
    
latitude = latlng(location)[0]
longitude = latlng(location)[1]

weather(latitude, longitude, location)
