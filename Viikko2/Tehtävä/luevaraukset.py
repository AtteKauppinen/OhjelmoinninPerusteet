"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""


def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        rivit = f.readlines()
    varaustenyhteishinta = 0.0
    for rivi in rivit:
        rivi = rivi.strip()
        if not rivi:
            continue
        # Jaetaan sisältö listaksi
        osat = rivi.split('|')
        varausnnumero = int(osat[0])
        varaaja = osat[1]
        paivamaara = osat[2]
        aloitusaika = osat[3]
        tuntimaara = int(osat[4])
        tuntihinta = float(osat[5])
        maksettu = "Kyllä" if osat[6].strip() == "True" else "Ei"
        kohde = osat[7]
        puhelin = osat[8]
        sahkoposti = osat[9]
        kokonaishinta = tuntimaara * tuntihinta
        varaustenyhteishinta += kokonaishinta
        # muotoillaan päivämäärä suomalaisittain
        from datetime import datetime
        paiva_obj = datetime.strptime(paivamaara, "%Y-%m-%d").date()
        suomalainenpaiva = paiva_obj.strftime("%d.%m.%Y")
        # muotoillaan aika suomalaisittain
        aika_obj = datetime.strptime(aloitusaika, "%H:%M").time()
        suomalainenaika = aika_obj.strftime("%H.%M")
        # Tulostetaan varaus konsoliin
        print(f"""Varausnumero: {varausnnumero}             
Varaaja: {varaaja}
Päivämäärä: {suomalainenpaiva}
Aloitusaika: {suomalainenaika}
Tuntimäärä: {tuntimaara}
Tuntihinta: {f'{tuntihinta:.2f}'.replace('.', ',')} €
Kokonaishinta: {f'{kokonaishinta:.1f} '.replace('.', ',')} €
Maksettu: {maksettu}
Kohde: {kohde}
Puhelin: {puhelin}
Sähköposti: {sahkoposti}
""")
    print(
        f"Varausten yhteishinta: {f'{varaustenyhteishinta:.2f}'.replace('.', ',')} €")

    # Tulostetaan varaus konsoliin

    # Kokeile näitä
    # print(varaus.split('|'))
    # varausId = varaus.split('|')[0]
    # print(varausId)
    # print(type(varausId))
    """
    Edellisen olisi pitänyt tulostaa numeron 123, joka
    on oletuksena tekstiä.

    Voit kokeilla myös vaihtaa kohdan[0] esim. seuraavaksi[1]
    ja testata mikä muuttuu
    """


if __name__ == "__main__":
    main()
