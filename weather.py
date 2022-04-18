import requests
import json

def check_conditions(zipcode):
    '''This function takes in a users zipcode and then inserts it into the weather api and stores all data into a json file'''
    weather_call = requests.get(
        f"http://api.weatherapi.com/v1/forecast.json?key=563c5fcd75104eca926161420221804&q={zipcode}&days=1&aqi=no&alerts=no")

    with open('weather.json', 'w') as outfile:
        json.dump(dict(weather_call.json()), outfile)
    

def weather_report():
    with open('weather.json') as readfile:
        data = json.load(readfile)
        city = data['location']['name']
        current_temp = int(data['current']["temp_f"])
        current_condition = data['current']["condition"]["text"]
    print(city)
    print(current_temp)
    print(current_condition)

check_conditions('san fran')
weather_report()