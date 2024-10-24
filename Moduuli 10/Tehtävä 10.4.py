import random
#Auto-luokka
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0
#Kiihdyttäminen
    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
#Auton kulkeminen
    def kuljettu(self, aika):
        self.kuljettu_matka += aika*self.nopeus
        return self.kuljettu_matka

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    #Tunnin kuluminen kilpailussa
    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kuljettu(1)

    #Autojen tilanne
    def tulosta_tilanne(self):
        tulokset = []
        for auto in self.autot:
            tulokset.append({
                "Rekisteritunnus": auto.rekisteritunnus,
                "Huippunopeus (km/h)": auto.huippunopeus,
                "Tämänhetkinen nopeus (km/h)": auto.nopeus,
                "Kuljettu matka (km)": auto.kuljettu_matka
            })

        # Tilanne taulukkona kuljetun matkan mukaan
        tulokset = sorted(tulokset, key=lambda x: x['Kuljettu matka (km)'], reverse=True)
        print(f"\nTilanne kilpailussa: {self.nimi}\n")
        for tulos in tulokset:
            print(f"Rekisteritunnus: {tulos['Rekisteritunnus']}, "
                  f"Huippunopeus: {tulos['Huippunopeus (km/h)']} km/h, "
                  f"Nopeus: {tulos['Tämänhetkinen nopeus (km/h)']} km/h, "
                  f"Kuljettu matka: {tulos['Kuljettu matka (km)']} km")
        print("\n")

    #Kilpailu ohi funktio
    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False

# Kilpailun ja autojen luominen ja suoritus
autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

# Kilpailun simulointi
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    kilpailu.tulosta_tilanne()

print("Kilpailu on päättynyt!")
