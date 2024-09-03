
tutkittva = int(input("Anna tutkittava luku: "))
alkuluku = True
for jakaja in range(2, tutkittva):
    if tutkittva % jakaja == 0:
        alkuluku = False
        break
if alkuluku:
    print("lukusi on alkuluku")
else:
    print("ei ole alkuluku")
