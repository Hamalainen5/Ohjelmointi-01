# Määritellään Auto-luokka
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0


# Luodaan pääohjelma
auto = Auto("ABC-123", 142,)

# Auto kiihdyttää
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

#tulostetaan auton nopeus
nykyinen_nopeus = auto.nopeus

#Suoritetaan hätäjarrutus
auto.kiihdyta(-200)

#Nopeus hätäjarrutuksen jälkeen
uusi_nopeus = auto.nopeus
print(f"Nopeus oli kiihdytyksien jälkeen {nykyinen_nopeus}, mutta hätäjarrutuksen jälkeen {uusi_nopeus}")




