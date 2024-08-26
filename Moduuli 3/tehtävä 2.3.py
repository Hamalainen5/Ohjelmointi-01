# Kysytään käyttäjältä hyttiluokkaa
hyttiluokka = input("Anna jokin seuraavista hyttiluokista A, B, C, LUX ").upper()
# annetaan hyttiluokan kuvaus
if hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
elif hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
else:
    print("virheellinen hyttiluokka"
          "")