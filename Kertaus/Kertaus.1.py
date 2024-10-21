print('hello world!')
print("hei, maailma!")
print("Hyvää\nhuomenta")
Kauttaja = input("Anna nimesi: ")
print("Hauska tavata, " + Kauttaja + "!")
print(Kauttaja)
eka = -9
toka = 12_456_123_180
kolmas = 4.973
neljas = -4 +2j
print(eka)
print(toka)
print(kolmas)
print(neljas)
print(kolmas.real)
print(neljas.imag)
fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit-32)*5/9
print("Lämpötila Celsius-asteina: " + str(celsius))
print(f"Lämpötila Celsius-asteina: {celsius:6.2f}")
import math
print(f"{'pii':12}: {math.pi:10.5f}")
print(f"{'Neperin luku':12s}:{math.e:10.5f}")

Ympyran_sade = float(input("Anna ympyrän säde: "))
Ympyran_pinta_ala =(Ympyran_sade/2)*math.pi**2
print("Ympyran pinta-ala: " + str(Ympyran_pinta_ala))

