import random
def heita_arpakuutioita():
    lukumaara = int(input("Kuinka monta arpakuutiota haluat heittää?"))

    summa = 0
    for i in range(lukumaara):
        silmaluku = random.randint(1, 6)
        summa += silmaluku
    print(summa)
heita_arpakuutioita()