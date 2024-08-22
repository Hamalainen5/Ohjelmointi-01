import random

# Kolmenumeroinen koodi (0-9)
kolmenumeroinen_koodi = ''.join(str(random.randint(0, 9)) for _ in range(3))

# Nelinumeroinen koodi (1-6)
nelinumeroiset_koodi = ''.join(str(random.randint(1, 6)) for _ in range(4))

# Tulostetaan koodit
print(f"Kolmenumeroinen koodi: {kolmenumeroinen_koodi}")
print(f"Nelinumeroinen koodi: {nelinumeroiset_koodi}")