import math
def karsi_parittomat(luvut):
    parilliset_luvut = [luku for luku in luvut if luku % 2 == 0]
    return parilliset_luvut
def paaohjelma():
    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu_lista = karsi_parittomat(alkuperainen_lista)
    print(alkuperainen_lista)
    print(karsittu_lista)
paaohjelma()