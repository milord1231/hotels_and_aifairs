import requests
import json
url = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"

querystring = {"rooms":"1","checkIn":"2021-01-27","checkOut":"2021-01-28","locale":"en_US","currency":"USD","include":"neighborhood"}

def get_town_data(town="", country=""):
    url = f"https://autocomplete.travelpayouts.com/places2?locale=ru&types[]=city&term={town}"
    req = requests.request("GET", url)
    return req.json()

def get_iata_codes(town=""):
    data = get_town_data(town=town)
    return data[0]['code']

def transform_iata_to_city(iata):
    pass

def get_aviafairs(origin, destination, departure_at, return_at, limit, page=1):
    data = {
        'currency ': "RUB",
        'origin ': get_iata_codes(origin),
        'destination': get_iata_codes(destination),
        'departure_at': departure_at,
        'return_at': return_at,
        'direct': "true",
        'market': "ru",
        'limit': limit,
        'page': "1",
        'sorting': "price",
        'uniqu': "false",
        'token': "eb241c69376140f3da72c23f7f1aa275",
        }
    response = requests.request("GET", url, params=data)
    if response:
        return response.json()
    return False

print(get_aviafairs('Новый Уренгой', 'Москва', '2023-03-13', '2023-03-14', 1))
