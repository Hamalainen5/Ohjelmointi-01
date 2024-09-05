# Anna bensiinin määrä gallonina
from operator import truediv


def gallonat_bensiiniksi():
    litrat = gallonat * 3.785
    print(f"Tämä on litroina: {litrat} litraa")

while True:
    gallonat = int(input("Anna bensiini gallonina: "))
    gallonat_bensiiniksi()
    if gallonat < 0:
        print("vaara vastaus:")
        break




