import requests
def check(key, word):
    for c in key:
        if c.get('countrie') == word:
            return print('Kraj został wybrany')
        return print("Kraj nie istnieje")

def build(country, countries):
    print(f"Wybrano kraj: {country}")
    print("Możesz zbudować:")
    print("1. Baraki, które szkolą żołnierzy")
    print("2. Odlewnię, która będzie budowała armaty")
    building = input("Co chcesz zbudować: ")

    if building == '1':
        for c in countries:
            if c.get['countrie'] == country and int(c['wood']) >= 1000:
                c['wood'] = str(int(c['wood']) - 1000)
                print("Zbudowano Baraki")
                print(c['wood'])
                update_country_on_server(c)
                break
        else:
            print("Niewystarczające zasoby drewna")

    elif building == '2':
        for c in countries:
            if c['countrie'] == country and int(c['steal']) >= 2000:
                c['steal'] = str(int(c['steal']) - 2000)
                print("Zbudowano Odlewnię")
                print(c['steal'])
                update_country_on_server(c)
                break
        else:
            print("Niewystarczające zasoby stali")
    else:
        print("Nieprawidłowy wybór budynku")

def update_country_on_server(country):
    response = requests.post("http://localhost:8000/update_country", json=country)
    if response.status_code == 200:
        print("Dane kraju zaktualizowane na serwerze.")
    else:
        print("Błąd podczas aktualizacji danych kraju na serwerze.")