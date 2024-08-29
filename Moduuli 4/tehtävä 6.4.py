# piin likiarvon laskeminen
# π≈4n/N, jossa n on yksikköympyrän sisälle osuvat pisteet, N on kaikki pisteet
# epäyhtälöllä x^2+y^2<1 tetstataan, onko yskittäinen piste ympyrän sisällä

# toinen tapa importata vain yskittäisiä toimijoita
# from random import randint
#randint(-1,1)
import math
import random
iteraor = 0
#todo: kysy N arvo käyttäjältä
N = 1000 # pisteiden kokonaismäärä
n = 0 # ympyrän sisään osuvat pisteet
while iteraor < N:
    iteraor += 1
    # arvotaan kordinaatit väliltä -1 ja 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    print(f"satunnainen piste: {x}, {y}")
    if x**2+y**2<1:
      print("osui ympyrän sisälle: ")
      n = n+1

print(f"{N} pisteestä {n} osui yksikköympyrän sisälle.")
result = 4 * n / N
print(f"Piin likiarvo on {result}")
print(f"virhe: {result - math.pi}")


