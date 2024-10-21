# Määritellään Auto-luokka
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 2000

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kuljettu(self, aika):
        self.kuljettu_matka += aika*self.nopeus
        return self.kuljettu_matka



auto = Auto("ABC-123", 142,)
auto.kiihdyta(60)
print(f"Auto on kulkenut aluksi 2000km, mutta jatkaa matkaa 60km/h 1.5h ajan,"
      f" jonka jälkeen se on kulkenut {auto.kuljettu(1.5)}km")





