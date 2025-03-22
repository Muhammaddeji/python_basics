import json

with open("009_data.json", "r") as json_file:
    car = json.load(json_file)

print(["brand"])

print(car.get("year"))

print(car["features"])

print(car["engine"] ["horsepower"])

car["year"] = 2025

print(car)

car["speed"] = "180km/h"

print(car.get("speed", "180km/h"))

car.update({"country": "japan"})

print(car)

del car ["colour"]

print(car)

model = car.pop("model")

print(car)

import json

with open("011_new_data", "w") as new_json:
    json.dump(car,  new_json)

print(len(car))

print(car.keys())

print(car.values())

print(car.items())

for key in car:
    print(key)

for key, value in car.items():
    print(key, value)


