# Määritellään Auto-luokka
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

# Luodaan pääohjelma
auto = Auto("ABC-123", 142)

# Tulostetaan auton ominaisuudet
auto_ominaisuudet = {
    "Rekisteritunnus": auto.rekisteritunnus,
    "Huippunopeus (km/h)": auto.huippunopeus,
    "Tämänhetkinen nopeus (km/h)": auto.nopeus,
    "Kuljettu matka (km)": auto.kuljettu_matka
}

print (f"Auton ominaisuudet ovat {auto_ominaisuudet}")
