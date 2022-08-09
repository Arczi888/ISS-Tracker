import json
import turtle
import urllib.request
import time

api = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(api)
result = json.loads(response.read())
astronauts = result["people"]

print(f"People currently in space: {len(astronauts)}")
print("-" * 40)

for astronaut in astronauts:
    print(f"{astronaut['name']} on {astronaut['craft']}")

window = turtle.Screen()
window.setup(720, 360)
window.title("Simple ISS Tracker")
window.setworldcoordinates(-180, -90, 180, 90)
window.bgpic("map.png")
window.register_shape("iss.gif")

iss = turtle.Turtle()
iss.shape("iss.gif")
iss.penup()

print("\nISS position:")
print("-" * 40)

while True:
    api = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(api)
    result = json.loads(response.read())

    iss_position = result["iss_position"]
    longitude = float(iss_position['longitude'])
    latitude = float(iss_position['latitude'])

    print(f"Longitude: {longitude}")
    print(f"Latitude: {latitude}\n")

    iss.goto(longitude, latitude)
    iss.pendown()

    time.sleep(5)
