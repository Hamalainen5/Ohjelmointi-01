# Tallennetaan käyttäjän syöttämät kaupungit listaan
kaupungit = []
for i in range (5):
    kaupunki = input("Anna jokin kaupunki:")
    kaupungit.append(kaupunki)
# Tulostetaan syötetyt kaupungit
print("Antamasi kaupungit")
for kaupunki in kaupungit:
    print(kaupunki)