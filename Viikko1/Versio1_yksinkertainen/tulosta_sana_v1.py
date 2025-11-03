# yksinkertainen esimerkki Python-ohjelmasta
# joka tulostaa tiedoston ja tulostaa sen sisältämän sanan.

# määritellään tiedoston polku suoraan koodissa
tiedosto = "sana.txt"

# avataan tiedosto lukemista varten
with open(tiedosto, "r", encoding="utf-8") as f:
    sana = f.read().strip()

# tulostetaan sana konsoliin
print(sana)
