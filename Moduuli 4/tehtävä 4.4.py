import random


def arvaa_luku():
    # Tietokone arpoo luvun väliltä 1..10
    arvottu_luku = random.randint(1, 10)

    while True:
        # Pelaajan arvaus
        arvaus = int(input("Arvaa luku väliltä 1..10: "))

        # Tarkistetaan pelaajan arvaus
        if arvaus > arvottu_luku:
            print("Liian suuri arvaus.")
        elif arvaus < arvottu_luku:
            print("Liian pieni arvaus.")
        else:
            print("Oikein! Arvottu luku oli:", arvottu_luku)
            break


# Käynnistetään peli
arvaa_luku()