kaupungit = []
kertaa = 0
while kertaa < 5:
    user_input = input("Anna kaupunki: ")
    kaupungit.append(user_input)
    kertaa += 1
for i in kaupungit:
    print(f"kaupungit olivat{i}")
