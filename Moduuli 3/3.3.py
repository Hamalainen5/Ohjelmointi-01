# ksysytään käyttäjän biologista sukupuolta
sukupuoli = input("ilmoita sukupuolesi mies/nainen: ")
# kysytään käyttäjän hemoglobiini arvoa
hemoglobiini = int(input("ilmoita hemoglobiinisi g/l: "))
if sukupuoli == "mies":
    alaraja = 134
    ylaraja = 195
elif sukupuoli == "nainen":
    alaraja = 117
    ylaraja = 175
else:
    print("virhe: tuntematon sukupuoli")
#tarkistetaan hemoglobiini
if alaraja < hemoglobiini < ylaraja:
    print("hemoglobiinisi on normaali")
elif hemoglobiini > ylaraja:
    print("hemoglobiinisi on korkea")
elif (hemoglobiini < alaraja):
    print("hemoglobiinisi on matala")
