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
#Pääohjelma
h = Elevator(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)


