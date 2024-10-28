#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.kuljettu_matka = 0
        self.nopeus = 0

    def aseta_nopeus(self, nopeus):
            self.nopeus = nopeus
            return self.nopeus

    # Kulje metodi
    def kuljettu(self, aika):
            self.kuljettu_matka += aika * self.nopeus
            return self.kuljettu_matka

    def tulosta_tiedot(self):
        print(f"Auton matkamittarin lukema on {self.kuljettu_matka}")

# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

        # Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.aseta_nopeus(130)
polttomoottoriauto.aseta_nopeus(135)
sahkoauto.kuljettu(3)
polttomoottoriauto.kuljettu(3)
sahkoauto.tulosta_tiedot()
polttomoottoriauto.tulosta_tiedot()












# Kirjoita aliluokille alustajat.
# Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh)
# ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus,
# käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.