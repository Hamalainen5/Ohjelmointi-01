# Sisäkkäiset toistorakenteet
eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1
    eka = eka + 1

import random
toistot = 0
heitot_yhteensä = 0
while toistot < 100000:
    noppa1 = noppa2 = heitot = 0
    while (noppa1!=6 or noppa2!=6):
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        heitot = heitot + 1
    toistot = toistot + 1
    heitot_yhteensä = heitot_yhteensä + heitot
heitot_keskimaarin = heitot_yhteensä/toistot
print(f"heitot keskimäärin: {heitot_keskimaarin:6.2f}")
