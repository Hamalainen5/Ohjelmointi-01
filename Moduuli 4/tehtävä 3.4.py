#lista lukujen säilyttämiseen
numero = []
#syötetään lukuja
while True:
    luku = input("anna lukuja, painamalla enter pysäytät toiminnon: ")
    if luku == '':
        break

    numero.append(float(luku))

if numero:
    print("suurin luku: ", max(numero))
    print("pienin luku: ", min(numero))
