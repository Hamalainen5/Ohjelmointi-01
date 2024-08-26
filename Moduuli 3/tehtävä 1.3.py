# Käyttäjä antaa kuhan pituuden
pituus = float(input("Anna kuhan pituus senttimetreinä: "))

alamitta = 37.0

# Tarkistetaan, onko kuha alamittainen
if pituus < alamitta:
    puuttuva = alamitta - pituus
    print(f"Kuha on alamittainen. Laske kuha takaisin järveen. Kuha on {puuttuva:.1f} cm liian lyhyt.")
else:
    print("Kuha on sopivan mittainen.")