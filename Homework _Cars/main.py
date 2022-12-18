import json

import uuid

if __name__ == '__main__':
    with open('cars.json') as json_file:
        data = json.load(json_file)

    new_cars = []

    for car in data:
        dict_car = dict(car)
        dict_car["ID"] = uuid.uuid4().hex

        new_cars.append(dict_car)

    slow_cars = [dict_car for dict_car in new_cars if dict_car.get("HP") < 120]

    fast_cars = [car for car in new_cars if 120 <= car.get("HP") < 180]

    sport_cars = [car for car in new_cars if car.get("HP") >= 180]

    cheap_price = [car for car in new_cars if car.get("Price") < 1000]

    medium_price = [car for car in new_cars if 1000 <= car.get("Price") < 5000]

    expensive_price = [car for car in new_cars if car.get("Price") >= 5000]

    bmw = [car for car in new_cars if car.get("Brand") == "BMW"]
    dacia = [car for car in new_cars if car.get("Brand") == "Dacia"]
    porsche = [car for car in new_cars if car.get("Brand") == "Porsche"]
    renault = [car for car in new_cars if car.get("Brand") == "Renault"]
    seat = [car for car in new_cars if car.get("Brand") == "Seat"]

    with open('output.data/slow_cars.json', 'w') as json_file:
        json.dump(slow_cars, json_file, indent=2)

    with open('output.data/fast_cars.json', 'w') as json_file:
        json.dump(fast_cars, json_file, indent=2)

    with open('output.data/sport_cars.json', 'w') as json_file:
        json.dump(sport_cars, json_file, indent=2)

    with open('output.data/cheap_cars.json', 'w') as json_file:
        json.dump(cheap_price, json_file, indent=2)

    with open('output.data/medium_cars.json', 'w') as json_file:
        json.dump(medium_price, json_file, indent=2)

    with open('output.data/expensive_cars.json', 'w') as json_file:
        json.dump(expensive_price, json_file, indent=2)

    with open('output.data/bmw_cars.json', 'w') as json_file:
        json.dump(bmw, json_file, indent=2)

    with open('output.data/dacia_cars.json', 'w') as json_file:
        json.dump(dacia, json_file, indent=2)

    with open('output.data/porsche_cars.json', 'w') as json_file:
        json.dump(porsche, json_file, indent=2)

    with open('output.data/renault_cars.json', 'w') as json_file:
        json.dump(renault, json_file, indent=2)

    with open('output.data/seat_cars.json', 'w') as json_file:
        json.dump(seat, json_file, indent=2)