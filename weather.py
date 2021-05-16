import threading
import requests
import sys
name = input("Tell me name of the city u want weather of: ")
sys.setrecursionlimit(1500)
def printit(name):

  threading.Timer(3600, printit, args=(name,)).start()
  response = requests.get("https://us1.locationiq.com/v1/search.php?key=pk.ae04ab12d7af9221ce03cf4393f03c1c&q="+name+"&format=json")
  lat = response.json()[0]['lat']
  long = response.json()[0]['lon']
  loc =  response.json()[0]['display_name']
  weather = requests.get("https://fcc-weather-api.glitch.me/api/current?lat="+str(lat)+"&lon="+str(long))

  data = weather.json()["main"]
  temp = data["temp"]
  status = weather.json()["weather"][0]["main"]
  print("Temperature for " +loc + " is " + str(temp) +" with " + status)

printit(name)