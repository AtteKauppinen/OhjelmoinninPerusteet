# Pieni python-ohjelma, joka lukee tiedoston ja tulostaa sen sisältämän sanan.
# tässä versiossa on main-funktio ja if __name__ == "__main__" -lohko.

def main():
    # määritellään tiedoston polku suoraan koodissa
    tiedosto = "sana.txt"

    # avataan tiedosto lukemista varten
    with open(tiedosto, "r", encoding="utf-8") as f:
        sana = f.read().strip()

    # tulostetaan sana konsoliin
    print(sana)


# tämä lohko varmistaa, että ohjelma suoritetaan vain,
# kun tiedostoa ajetaan suoraan, ei tuottaessa moduulina.
if __name__ == "__main__":
    main()
