import math
suorakulmion_kanta_str = input("Anna suorakulmion kanta: ")
suorakulmion_kanta = float(suorakulmion_kanta_str)
suorakulmion_korkeus_str = input("Anna suorakulmion korkeus: ")
suorakulmion_korkeus = float(suorakulmion_korkeus_str)
Suorakulmion_pintaala = suorakulmion_kanta * suorakulmion_korkeus
print("suorakulmion pinta-ala on")
print(Suorakulmion_pintaala)

suorakulmion_piiri = suorakulmion_kanta * 2 +suorakulmion_korkeus * 2
print("suorakulmion piiri on")
print(suorakulmion_piiri)
