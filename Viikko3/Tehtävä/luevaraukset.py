"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin käyttäen funkitoita.
Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19,95 €
Kokonaishinta: 39,9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""
from datetime import datetime

# Funktioita jokaiselle tiedolle


def hae_varaaja(varaus):
    nimi = varaus[1]
    print(f"Varaaja: {nimi}")


def hae_varausnumero(varaus):
    varausnumero = int(varaus[0])
    print(f"Varausnumero: {varausnumero}")


def hae_paiva(varaus):
    paivamaara = varaus[2]
    paiva_obj = datetime.strptime(paivamaara, "%Y-%m-%d").date()
    suomalainenpaiva = paiva_obj.strftime("%d.%m.%Y")
    print(f"Päivämäärä: {suomalainenpaiva}")


def hae_aloitusaika(varaus):
    aloitusaika = varaus[3]
    aika_obj = datetime.strptime(aloitusaika, "%H:%M").time()
    suomalainenaika = aika_obj.strftime("%H.%M")
    print(f"Aloitusaika: {suomalainenaika}")


def hae_tuntimaara(varaus):
    tuntimaara = int(varaus[4])
    print(f"Tuntimäärä: {tuntimaara}")


def hae_tuntihinta(varaus):
    tuntihinta = float(varaus[5])
    print(f"Tuntihinta: {f'{tuntihinta:.2f}'.replace('.', ',')} €")


def laske_kokonaishinta(varaus):
    tuntimaara = int(varaus[4])
    tuntihinta = float(varaus[5])
    kokonaishinta = tuntimaara * tuntihinta
    print(f"Kokonaishinta: {f'{kokonaishinta:.1f} '.replace('.', ',')}€")


def hae_maksettu(varaus):
    maksettu = "Kyllä" if varaus[6].strip() == "True" else "Ei"
    print(f"Maksettu: {maksettu}")


def hae_kohde(varaus):
    kohde = varaus[7]
    print(f"Kohde: {kohde}")


def hae_puhelin(varaus):
    puhelin = varaus[8]
    print(f"Puhelin: {puhelin}")


def hae_sahkoposti(varaus):
    sahkoposti = varaus[9]
    print(f"Sähköposti: {sahkoposti}")


def main():
    # Maaritellaan tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto, luetaan tiedosto riveittäin ja käsitellään jokainen rivi
    with open(varaukset, "r", encoding="utf-8") as f:
        rivit = f.readlines()
    for rivi in rivit:
        rivi = rivi.strip()
        if not rivi:
            continue
        varaus = rivi.split('|')
        # Toteuta loput funktio hae_varaaja(varaus) mukaisesti
        # Luotavat funktiota tekevat tietotyyppien muunnoksen
        # ja tulostavat esimerkkitulosteen mukaisesti
        hae_varausnumero(varaus)
        hae_varaaja(varaus)
        hae_paiva(varaus)
        hae_aloitusaika(varaus)
        hae_tuntimaara(varaus)
        hae_tuntihinta(varaus)
        laske_kokonaishinta(varaus)
        hae_maksettu(varaus)
        hae_kohde(varaus)
        hae_puhelin(varaus)
        hae_sahkoposti(varaus)
        print("")


if __name__ == "__main__":
    main()
