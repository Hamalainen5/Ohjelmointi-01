import math


def calculate_square_price(diameter, price):
    #muutetaan sentit metreiksi
    diameter = diameter / 100
    # pizzan pinta-ala on pi*r^2
    r = diameter / 2
    area = math.pi * r * r
    return price / area

# pääohjelma
pizza1_diameter = float(input("Syötä 1. pizzan halkaisija senttimetreinä: "))
pizza2_diameter = float(input("Syötä 2. pizzan halkaisija senttimetreinä: "))
pizza1_price = float(input("Syötä 1. pizzan hinta euroina: "))
pizza2_price = float(input("Syötä 2. pizzan hinta euroina: "))

pizza1_square_price = calculate_square_price(pizza1_diameter, pizza1_price)
pizza2_square_price = calculate_square_price(pizza2_diameter, pizza2_price)

print(f"Ensimmäisen pizzan neliöhinta on {pizza1_square_price:.2f}")
print(f"Toisen pizzan neliöhinta on {pizza2_square_price:.2f}")

if pizza1_square_price < pizza2_square_price:
    print("Ensimmäinen pizza on halvempi")
elif pizza1_square_price > pizza2_square_price:
    print("Toinen pizza on halvempi")
else:
    print("Pizzojen neliöhinta on sama")

