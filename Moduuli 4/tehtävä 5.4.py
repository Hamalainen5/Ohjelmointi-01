def kirjautuminen ():
    oikea_kayttajatunnus = "python"
    oikea_salasana = "rules"
    #sallittu yritysten määrä
    max_yritykset = 5
    yritykset = 0
    while yritykset < max_yritykset:
        kauttajatunnus = input("Anna kauttajatunnus: ")
        salasana = input("Anna salasana: ")
        if kauttajatunnus == "python" and salasana == "rules":
            print("kirjautuminen onnistui")
        else:
            yritykset += 1
            print("vaara kauttajatunnus tai salasana: ")
    print("pääsy evätty")
kirjautuminen()