import random
# kysytään käyttäjältä tahkojen määrä
tahkojen_maara = int(input("Tahkojen maara : "))
def heita_noppa():
    return random.randint(1,tahkojen_maara)
def paaohjelma():
    silmaluku = 0
    while silmaluku != tahkojen_maara:
        silmaluku = heita_noppa()
        print(f"heitit: {silmaluku}")
if __name__ == '__main__':
    paaohjelma()