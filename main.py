import requests

#open weathermap api
OWM = 'https://api.openweathermap.org/data/2.5/onecall'


#YOUR API HERE
api=YOUR API HERE


#parameters for the api
parameters = {
    'lat': float(45.512230),
    'lon': float(-122.658722),
    'appid': api,
    'exclude': ''
}

#getting the json from the api
response = requests.get(OWM, params=parameters)
response.raise_for_status()
weather = response.json()

#slicing the data we need form the weather json
weather_slice = weather['hourly'][:12]

#For loop to the weather condition
for hour in weather_slice:
    condition = hour['weather'][0]['id']
    if int(condition) <700:
        print('wear a jacket')
    else:
        print('clear skies')
