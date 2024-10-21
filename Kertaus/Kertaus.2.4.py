#While/else
komento = input("Anna komento: ")
while komento !="lopeta":
    if komento == "MAYDAY":
        break
    print("suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
else:
    print("Näkemiin.")
print("Toiminnot lopetettu.")
