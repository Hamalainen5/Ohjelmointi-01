def lentoasemaohjelma():
    # esiasetetut lentoasemat(ICAO-koodi ja lentoaseman nimi)

    lentoasemat = {"EFHK": "Helsinki-Vantaa",
        "EHAM": "Amsterdam Schiphol",
        "KJFK": "John F. Kennedy International Airport",
        "EGLL": "London Heathrow",
        "EDDF": "Frankfurt Airport"}
    while True:
        # käyttäjä valitsee toiminnon
        print("\nValitse toiminto:")
        print("1. Syötä uusi lentoasema")
        print("2. Hae lentoaseman tiedot")
        print("3. Lopeta ohjelma")

        valinta = input("Syötä valintasi (1/2/3): ")
        if valinta == "1":
            icao = input("Anna lentoaseman ICAO_koodi: ")
            nimi = input("Anna lentoaseman nimi: ")

            if icao in lentoasemat:
                print(f"Lentoasema {icao} on jo tallennettu nimellä{lentoasemat[icao]}")
            else:
                lentoasemat[icao] = nimi
                print(f"Lentoasema {icao}{nimi} lisätty. ")
        elif valinta == "2":
            #lentoasema tietojen haku
            icao = input("Anna haettavan lentoaseman ICAO_koodi: ")
            if icao in lentoasemat:
                print(f"Lentoasema {icao}: {lentoasemat[icao]}")
            else:
                print(f"Lentoasema ICAO-koodilla {icao} ei löytynyt.")
        elif valinta == "3":
            #ohjelman lopetus
            print("ohjelma lopetetaan")
            break
        else:
            print("virhe, yritä uudelleen")
#kutsutaan funktio
lentoasemaohjelma()


