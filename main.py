import requests
import io
import ctypes
import time
from PIL import Image , ImageDraw , ImageFont

#Send Request
api_key = 'e1d9972099ddabf1105ce9cd789d3e11'
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Dubai&units=metric&APPID={api_key}")

#Get needed info and format
degree_sign= u'\N{DEGREE SIGN}'
rawTempInt = weather_data.json()['main']['temp']
weather = "Weather: " + weather_data.json()['weather'][0]['description'].capitalize()
tempString = "Temperature: " + str(round(weather_data.json()['main']['temp'])) + degree_sign
feelTemp = "Feels Like: " + str(round(weather_data.json()['main']['feels_like'])) + degree_sign
icon = weather_data.json()['weather'][0]['icon']
parameters_in_one = weather + "\n" + tempString + "\n" + feelTemp + "\n"


if(rawTempInt <= 30):
    status = 1
elif(30 < rawTempInt < 34):
    status = 2
elif(34 <= rawTempInt < 37):
    status = 3
elif(37 <= rawTempInt < 40):
    status = 4
else:
    status = 5

pathToImage = "C:\\Users\\osaid\\Desktop\\Python\\WeatherBackgroundChanger\\background_images\\" + str(status) + ".jpg"
image = Image.open(pathToImage)
font = ImageFont.truetype('C:\\Users\\osaid\\Desktop\\Python\\WeatherBackgroundChanger\\Lobster-Regular.ttf', 40)

#Draw the box over background
draw = ImageDraw.Draw(image , 'RGBA')
box = draw.rectangle([100,100,750,300] , fill = (128,128,128,100) , outline = 'black')

#Write text
draw.text((120,120) , parameters_in_one , font = font)

#Icon retrieve
requestIcon = requests.get('http://openweathermap.org/img/wn/' + icon + '@4x.png')
image_bytes = io.BytesIO(requestIcon.content)
iconImage = Image.open(image_bytes).convert('RGBA')
#paste icon
image.paste(iconImage, (550,100), iconImage)
image.save('C:\\Users\\osaid\\Desktop\\Python\\WeatherBackgroundChanger\\background_images\\' + str(status) + ".png")
time.sleep(3)

#Set wallpaper function
SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE   = 0x2 
wallpaperPath = r"C:\Users\osaid\Desktop\Python\WeatherBackgroundChanger\background_images\\" + str(status) + ".png"
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0,wallpaperPath,SPIF_UPDATEINIFILE)

