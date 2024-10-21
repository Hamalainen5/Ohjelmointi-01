# Määritellään Auto-luokka
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0
#Kiihdytä metodi
    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
#Kulje metodi
    def kuljettu(self, aika):
        self.kuljettu_matka += aika*self.nopeus
        return self.kuljettu_matka

import random

autot = []
kilpailu_kaynnissa = True
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))
#Kilpailu alkaa
while kilpailu_kaynnissa:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)

        #Auto liikkuu tunnin ajan
        auto.kuljettu(1)

        #Tarkistetaan onko auto kulkenut vähintään 10000km
        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False
            break
#Tulostetaan tulokset
tulokset = []
for auto in autot:
    tulokset.append({
        "Rekisteritunnus": auto.rekisteritunnus,
        "Huippunopeus (km/h)": auto.huippunopeus,
        "Tämänhetkinen nopeus (km/h)": auto.nopeus,
        "Kuljettu matka (km)": auto.kuljettu_matka
    })


# Tulostetaan lopputulokset taulukkomuodossa, järjestettynä kuljetun matkan mukaan (suurimmasta pienimpään)
tulokset = sorted(tulokset, key=lambda x: x['Kuljettu matka (km)'], reverse=True)

# Tulostetaan taulukko
for tulos in tulokset:
    print(f"Rekisteritunnus: {tulos['Rekisteritunnus']}, "
          f"Huippunopeus: {tulos['Huippunopeus (km/h)']} km/h, "
          f"Nopeus: {tulos['Tämänhetkinen nopeus (km/h)']} km/h, "
          f"Kuljettu matka: {tulos['Kuljettu matka (km)']} km")
