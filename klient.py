import requests

WOOD_FOR_BARAK=1000

def country_exists(countries, country_id):
    return 0<=country_id<len(countries)

def build(country_id, country):
    print(f"Wybrano kraj: {country['name']}")
    print("Możesz zbudować:")
    print("1. Baraki, które szkolą żołnierzy")
    print("2. Odlewnię, która będzie budowała armaty")
    building = input("Co chcesz zbudować: ")

    if building == '1':
        if country['wood'] >= WOOD_FOR_BARAK:
            country['wood'] -= WOOD_FOR_BARAK
            print("Zbudowano Baraki")
            print(country['wood'])
            update_country_on_server(country_id,country)
        else:
            print("Niewystarczające zasoby drewna")

    elif building == '2':
        if country['steel']>= 2000:
            country['steel'] -=2000
            print("Zbudowano Odlewnię")
            print(country)
            update_country_on_server(country_id,country)
        else:
            print("Niewystarczające zasoby stali")
    else:
        print("Nieprawidłowy wybór budynku")

def update_country_on_server(country_id,country):
    response = requests.post(f"http://localhost:8000/update_country/{country_id}", json=country)
    if response.status_code == 200:
        print("Dane kraju zaktualizowane na serwerze.")
    else:
        print("Błąd podczas aktualizacji danych kraju na serwerze.")

response = requests.get('http://127.0.0.1:8000/countries')
countries = response.json()
print("Lista krajów:")
for i,country in enumerate(countries):
    print(i,country.get('name'))

while True:
    country_id = int(input("Wybierz kraj: "))
    if country_exists(countries, country_id):
        print("Kraj został wybrany.")
        build(country_id, countries[country_id])
    else:
        print("Niepoprawny kraj. Wybierz kraj z listy.")