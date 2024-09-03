import random
# kysytään käyttäjältä heittojen lukumäärää
lukumaara = int(input("anna heittojen lukumäärä:"))
summa = 0
for i in range(lukumaara):
    heitto = random.randint(1,6)
    summa += heitto
print(f"heittojen summa: {summa}")