#Hissi luokka
class Elevator:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros
    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo ylimmässä kerroksessa")
    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo alimmassa kerroksessa")
    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros > self.nykyinen_kerros:
            while self.nykyinen_kerros < kohde_kerros:
                self.kerros_ylös()
        elif kohde_kerros < self.nykyinen_kerros:
            while self.nykyinen_kerros > kohde_kerros:
                self.kerros_alas()
        else:
            print(f"Hissi on jo kerroksessa {kohde_kerros}.")
class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.hissit = [Elevator(alin_kerros, ylin_kerros) for i in range(hissien_lukumaara)]
    def aja_hissia(self, hissi_numero, kohde_kerros):
        if 1 <= hissi_numero <= len(self.hissit):
            print(f"Ajetaan hissiä {hissi_numero} kohdekerrokseen {kohde_kerros}.")
            self.hissit[hissi_numero - 1].siirry_kerrokseen(kohde_kerros)
        else:
            print(f"Hissi numero {hissi_numero} ei ole olemassa.")
 # Pääohjelma
talo = Talo(1, 10, 3)  # Talo, jossa on kerrokset 1-10 ja 3 hissiä

# Ajetaan hissiä 1 viidenteen kerrokseen
talo.aja_hissia(1, 5)

# Ajetaan hissiä 2 seitsemänteen kerrokseen
talo.aja_hissia(2, 7)

# Ajetaan hissiä 3 alimpaan kerrokseen (1)
talo.aja_hissia(3, 1)
