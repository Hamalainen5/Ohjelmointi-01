kauttajatunnus = ("koira")
salasana = ("kissa")
yritykset = 0
while yritykset != 5:
    kysytaan_kauttajatunnus = input("Anna kauttajatunnus: ")
    kysytaan_salasana = input("Anna salasana: ")
    if kysytaan_kauttajatunnus not in kauttajatunnus and kysytaan_salasana not in salasana:
        yritykset += 1
    else:
        print("Tervetuloa!")
        break






