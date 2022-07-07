import requests
import time
# This program sets the Nanoleaf to theme base on the current weather at UH Manoa
# Works for Sunny, Cloudy, Rain, Snow, Fog/Smoke, Lightning, Nighttime, Sunrise and Sunset


# Returns a time code representing the time of day
# Night = 0, sunrise = 1, day = 2, sunset = 3, error = -1
def TimeOfDay(timeNow, sunrise, sunset):
    timeCode = 0
    if timeNow < sunrise - seconds:
        # print("Night")
        timeCode = 0
    elif sunrise - seconds < timeNow < sunrise + seconds:
        timeCode = 1
    elif sunrise + seconds < timeNow < sunset - seconds:
        # print("Day")
        timeCode = 2
    elif sunset - seconds < timeNow < sunset + seconds:
        # print("Sunset")
        timeCode = 3
    elif timeNow > sunset + seconds:
        # print("Night")
        timeCode = 0
    else:
        print("Error: Time of Day")
        timeCode = -1
    return timeCode


# Sets the lights to theme based on weather
# Themes called:
# Night, Lightning, Sunrise, Sunset, Rainy Day, Snowfall, Fog, Sunny, Cloudy day, Lightning
# must be downloaded to nanoleaf
def SetLights(weatherCode, timeCode):
    # weatherCode = 300
    print("Setting Lights")
    url = "http://192.168.1.108:16021/api/v1/ulczMjy1KbTMxjHjM0UyQjevoUOMzbaO/effects"
    headers = {}
    if timeCode == 0:
        if 200 < weatherCode < 200:
            print("Night Thunderstorm")
            payload = "{\"select\" : \"Lightning\"}"
            response = requests.request("PUT", url, headers=headers, data=payload)
            print(response.text)
        else:
            print("Night")
            payload = "{\"select\" : \"Night\"}"
            response = requests.request("PUT", url, headers=headers, data=payload)
            print(response.text)
    elif timeCode == 1:
        print("Sunrise")
        payload = "{\"select\" : \"Sunrset\"}"
        response = requests.request("PUT", url, headers=headers, data=payload)
        print(response.text)
    elif timeCode == 2:
        print("Day")
        if 200 < weatherCode < 300:
            print("Thunderstorm")
            payload = "{\"select\" : \"Lightning\"}"
            response = requests.request("PUT", url, headers=headers, data=payload)
            print(response.text)
        elif 300 <= weatherCode < 600:
            print("Rain")
            payload = "{\"select\" : \"Rain\"}"
            response = requests.request("PUT", url, headers=headers, data=payload)
            print(response.text)
        elif 600 <= weatherCode < 700:
            print("Snow")
            payload = "{\"select\" : \"Snowfall\"}"
            response = requests.request("PUT", url, headers=headers, data=payload)
            print(response.text)
        elif 700 <= weatherCode < 800:
            print("Atmospheric Conditions")
            payload = "{\"select\" : \"Fog\"}"
            response = requests.request("PUT", url, headers=headers, data=payload)
            print(response.text)
        elif weatherCode == 800:
            print("Clear")
            payload = "{\"select\" : \"Blue Sky\"}"
            response = requests.request("PUT", url, headers=headers, data=payload)
            print(response.text)
        elif weatherCode == 801 or weatherCode == 802:
            print("Few Clouds")
            payload = "{\"select\" : \"Few Clouds\"}"
            response = requests.request("PUT", url, headers=headers, data=payload)
            print(response.text)
        elif weatherCode == 803:
            print("Broken Clouds")
            payload = "{\"select\" : \"Broken Clouds\"}"
            response = requests.request("PUT", url, headers=headers, data=payload)
            print(response.text)
        elif weatherCode == 804:
            print("Cloudy")
            payload = "{\"select\" : \"Cloudy\"}"
            response = requests.request("PUT", url, headers=headers, data=payload)
            print(response.text)
        elif 805 <= weatherCode < 900:
            print("Cloudy")
            payload = "{\"select\" : \"Cloudy\"}"
            response = requests.request("PUT", url, headers=headers, data=payload)
            print(response.text)
    elif timeCode == 3:
        print("Sunset")
        payload = "{\"select\" : \"Sunset\"}"
        response = requests.request("PUT", url, headers=headers, data=payload)
        print(response.text)
    else:
        print("Error")


# Sets the Brightness Based on a temperature
def SetBrightness(temp):
    print("Setting Brightness")
    intensity = mapRange(temp, 273, 300, 20, 100)
    if intensity < 20:
        intensity = 20
    if intensity > 100:
        intensity = 100
    print(intensity)
    url = "http://192.168.1.108:16021/api/v1/ulczMjy1KbTMxjHjM0UyQjevoUOMzbaO/state"

    payload1 = "{\"brightness\" : {\"value\":"
    payload2 = "}}"
    payload =  (payload1 + str(int(intensity)) + payload2)
    headers = {}
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)

    #Display the current brightness below
    url = "http://192.168.1.108:16021/api/v1/ulczMjy1KbTMxjHjM0UyQjevoUOMzbaO/state/brightness"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


# Maps a value to a range
def mapRange(value, inMin, inMax, outMin, outMax):
    return outMin + (((value - inMin) / (inMax - inMin)) * (outMax - outMin))


# api_address = 'https://api.openweathermap.org/data/2.5/weather?lat=55.7512&lon=37.6184&appid=5ab259cc1c9d2498547d62bcbe5200cd' # Moscow
# api_address = 'https://api.openweathermap.org/data/2.5/weather?lat=21.26146&lon=-157.82093&appid=5ab259cc1c9d2498547d62bcbe5200cd' # Shaka Cam Elks honolulu
# api_address = 'https://api.openweathermap.org/data/2.5/weather?lat=21.2969&lon=-157.8171&appid=5ab259cc1c9d2498547d62bcbe5200cd' # UH Manoa
# api_address = 'https://api.openweathermap.org/data/2.5/weather?lat=71.113180&lon=25.82576&appid=5ab259cc1c9d2498547d62bcbe5200cd' # Skarsvåg, Norway
# api_address = 'https://api.openweathermap.org/data/2.5/weather?lat=62.29942&lon=7.261230&appid=5ab259cc1c9d2498547d62bcbe5200cd' # Grunnfarnesbotn Fjord, Norway
# https://www.webcamtaxi.com/en/norway/troms/grunnfarnesbotn-fjord.html

api_address = 'https://api.openweathermap.org/data/2.5/weather?lat=64.1942&lon=-51.6735828&appid=5ab259cc1c9d2498547d62bcbe5200cd' # Nuuk Airport, Greenland

seconds = 600
json_data = requests.get(api_address).json()
weatherCode1 = json_data['weather'][0]['id']
weatherCode2 = -1

timeCode1 = -1
timeCode2 = -1

##############################################
# Nanoleafs
# api key ulczMjy1KbTMxjHjM0UyQjevoUOMzbaO
##############################################

starttime = time.time()
while True:
    print("Updating Weather Data...")
    timeNow = int(time.time())
    json_data = requests.get(api_address).json()
    weatherCode1 = weatherCode2
    weatherCode2 = json_data['weather'][0]['id']
    sunrise = json_data['sys']['sunrise']
    sunset = json_data['sys']['sunset']
    temperature = json_data['main']['temp']
    print(json_data['weather'][0]['description'])
    print(sunrise)
    print(timeNow)
    print(temperature)
    # print(weatherCode1)
    print(weatherCode2)
    timeCode1 = timeCode2
    timeCode2 = TimeOfDay(timeNow, sunrise, sunset)
    # print(timeCode1)
    print(timeCode2)

    # if timeCode1 != timeCode2 or weatherCode1 != weatherCode2:
    #    SetLights(weatherCode2, timeCode2)

    SetLights(weatherCode2, timeCode2)
    SetBrightness(temperature)
    
    # Display current effect
    url = "http://192.168.1.108:16021/api/v1/ulczMjy1KbTMxjHjM0UyQjevoUOMzbaO/effects/select"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print("current effect")
    print(response.text)

    time.sleep(10.0 - ((time.time() - starttime) % 10.0))
