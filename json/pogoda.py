
import requests

miasto = input("Poddaj maisto: ")


def pobranie_lokalizacji(mistao):
    # pobieram numer lokalizacji
    resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={miasto}")
    # print(resp.json())
    nr_miasto = resp.json()[0]['woeid']
    return nr_miasto


nr_miasto = pobranie_lokalizacji(miasto)

# pobieram pogode dla lokalizacji
resp2 = requests.get(f"https://www.metaweather.com/api/location/{nr_miasto}/")

# prognoza = resp2.json()
print(resp2.json())

pogoda = resp2.json()['consolidated_weather'][0]
print(pogoda)

# drukuje pogoda

print("temperatura", pogoda['the_temp'])
print("cisnienie", pogoda['air_pressure'])