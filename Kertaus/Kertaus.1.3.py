import random

leiviska = int(input("Anna leiviskät: "))
naula = int(input("Anna naulat: "))
luodit = int(input("Anna luodit: "))

leiviska_gr = 20*32*13.3*naula
naula_gr = 32*13.3*luodit
luoti_gr = 13.3*luodit

Paino_yht = leiviska_gr + naula_gr + luoti_gr
print(Paino_yht)

import random
kolmenumeroinen_koodi = [random.randint(0, 9) for i in range(3)]
nelinumeroinen_koodi = [random.randint(0, 6) for i in range(4)]
print(kolmenumeroinen_koodi)
print(nelinumeroinen_koodi)
