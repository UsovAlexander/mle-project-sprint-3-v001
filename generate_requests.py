import requests
import time
import random

for i in range(40):
    url = f'http://127.0.0.1:8081/api/price/?flat_id={i}'
    headers = {'accept': 'application/json',
           'Content-Type': 'application/json'
           }

    model_params = {
        "floor": random.randint(1, 10),
        "is_apartment": random.randint(0, 1),
        "kitchen_area": random.uniform(5.0, 15.0),
        "living_area": random.uniform(10.0, 30.0),
        "rooms": random.randint(1, 5),
        "studio": random.randint(0, 1),
        "total_area": random.uniform(30.0, 100.0),
        "build_year": random.randint(1950, 2022),
        "building_type_int": random.randint(1, 10),
        "latitude": random.uniform(55.6, 55.8),
        "longitude": random.uniform(37.6, 37.8),
        "ceiling_height": random.uniform(2.5, 3.5),
        "flats_count": random.randint(50, 100),
        "floors_total": random.randint(5, 20),
        "has_elevator": random.randint(0, 1)
    }

    response = requests.post(url, headers=headers, json=model_params)
    print(response)
    if i == 30:
        time.sleep(30)
    time.sleep(10)

for i in range(10):
    url = f'http://127.0.0.1:8081/api/price/?flat_id={i}'
    headers = {'accept': 'application/json',
        'Content-Type': 'application/json'
        }

    model_params = {}

    response = requests.post(url, headers=headers, json=model_params)
    print(response)
    time.sleep(10)