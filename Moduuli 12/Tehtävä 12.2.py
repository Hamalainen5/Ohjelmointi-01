import requests


def hae_saa(api_key):
    # Kysytään käyttäjältä kaupungin nimi
    kaupunki = input("Anna kaupungin nimi, jonka säätiedot haluat nähdä: ").capitalize()

    # OpenWeatherMap API:n perus-URL
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Parametrit API-pyyntöön
    params = {
        'q': kaupunki,
        'appid': api_key,
        'units': 'metric',  # Celsius-asteina
        'lang': 'fi'  # Suomenkielinen tulos
    }

    # Lähetä pyyntö API:lle
    vastaus = requests.get(base_url, params=params)

    # Tarkista, että pyyntö onnistui
    if vastaus.status_code == 200:
        data = vastaus.json()

        # Tulostetaan muutama tärkeä sääparametri
        print(f"Sää {kaupunki}-alueella:")
        print(f"Lämpötila: {data['main']['temp']} °C")
        print(f"Kuvaus: {data['weather'][0]['description']}")
        print(f"Kosteus: {data['main']['humidity']}%")
        print(f"Tuulen nopeus: {data['wind']['speed']} m/s")
    else:
        print("Virhe haettaessa säätietoja. Tarkista kaupungin nimi ja yritä uudelleen.")


# Esimerkki käyttö
api_key = "Api-key"  # Syötä oma API-avain tähän
hae_saa(api_key)
