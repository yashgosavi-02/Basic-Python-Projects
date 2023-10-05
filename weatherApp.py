import requests
import json
import pyttsx3

city = input("Enter Name of the City = ")
url = f"https://api.weatherapi.com/v1/current.json?key=f7aa4169bf6047d6a0992015230510&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
temp = wdic["current"]["temp_c"]
cond = wdic["current"]["condition"]["text"]
# print(r.text)
sys = pyttsx3.init()
sys.say(f"The current weather in {city} is {temp} degrees and Condition is {cond}")
sys.runAndWait()

# API KEY = f7aa4169bf6047d6a0992015230510
