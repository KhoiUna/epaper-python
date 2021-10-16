import requests

def get_weather():
    file = open('weather.env.txt', 'r')
    API_key = file.read()
    file.close()

    url = "https://api.openweathermap.org/data/2.5/weather?appid=" + \
        API_key + "&zip=35632&units=imperial"
    
    temp = requests.get(url).json()['main']['temp']
    return temp

# print(get_weather())