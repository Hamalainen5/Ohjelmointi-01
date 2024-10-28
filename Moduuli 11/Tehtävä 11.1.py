#Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi.
class Julkaisu:
    def __init__(self, name):
        self.name = name

# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
class Kirja(Julkaisu):
    def __init__(self, name, sivumaara, kirjoittaja):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(name)
    def tulosta_tiedot(self):
        print(f"Kirjan {self.name} on kirjoittanut {self.kirjoittaja} ja siinä on {self.sivumaara}-sivua")

class Lehti(Julkaisu):
    def __init__(self, name, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(name)
    def tulosta_tiedot(self):
        print(f"Lehden {self.name} päätoimittaja on {self.paatoimittaja}")

aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti = Kirja("Hytti n:o 6", 200, "Rosa Liksom")
hytti.tulosta_tiedot()
aku_ankka.tulosta_tiedot()





# Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.
