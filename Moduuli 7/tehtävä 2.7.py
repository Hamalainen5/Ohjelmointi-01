#kysytään käyttäjältä nimet
nimet = set()
while True:
    nimi =input("Sijoita jokin nimi, painamalla enter lopetat toiminnon: ")
    if nimi == "":
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi, syötä uusi nimi:")

    else:
        print("uusi nimi:")
        nimet.add(nimi)

print("antamasi nimet ovat: ")
print(nimet)

