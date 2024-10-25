import numpy as np
print("Tässä ensimmäinen tehtävä, jossa muunnetaan radiaanit asteiksi")

A = np.array([2.493, 0.911])

for i in A:
  print(f"Asteet: {np.degrees(i)}")

print("Tässä toinen tehtävä, jossa muunnetaan asteet radiaaneiksi")
B = np.array([137.7, 62.3])

for i in B:
  print(f"Radiaanit: {np.radians(i)}")

print("Ja kolmas pisin tehtävä")
C = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for i in C:
  print(f"Radiaanit: {np.radians(i)}")