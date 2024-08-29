# Määritellään muuntokerroin
INCH_TO_CM = 2.54

while True:
    # Pyydetään käyttäjää syöttämään tuumamäärä
    inches = float(input("Anna tuumamäärä (negatiivinen luku lopettaa ohjelman): "))

    # Tarkistetaan, onko syötetty luku negatiivinen
    if inches < 0:
        print("Ohjelma lopetetaan.")
        break

    # Lasketaan ja tulostetaan muunnos
    centimeters = inches * INCH_TO_CM
    print(f"{inches} tuumaa on {centimeters:.2f} senttimetriä")