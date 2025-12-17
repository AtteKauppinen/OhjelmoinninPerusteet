# Copyright (c) 2025 Atte Kauppinen
# License: MIT

"""Sähkönkulutuksen ja -tuotannon käsittelyä CSV-tiedostosta. Kirjoittaa sähkökulutus- ja sähkötuotantoyhteenvedon tiedostoon."""

from datetime import datetime, date


def muunna_tiedot(kulutustuotanto: list) -> list:
    """ Muuttaa tiedostossa annetut tietorivin tietotyypit oikeiksi tietotyypeiksi
    parametrit: kulutustuotanto: lista, jossa on 7 kenttää.
    Ensimmäinen kenttä on päivämäärä ja loput kuusi kenttää ovat kokonaislukuja.

    palauttaa: lista, jossa on muutetut tietotyypit
    """
    muutettu_tietorivi = []
    muutettu_tietorivi.append(datetime.fromisoformat(kulutustuotanto[0]))
    muutettu_tietorivi.append(int(kulutustuotanto[1]))
    muutettu_tietorivi.append(int(kulutustuotanto[2]))
    muutettu_tietorivi.append(int(kulutustuotanto[3]))
    muutettu_tietorivi.append(int(kulutustuotanto[4]))
    muutettu_tietorivi.append(int(kulutustuotanto[5]))
    muutettu_tietorivi.append(int(kulutustuotanto[6]))
    return muutettu_tietorivi


def lue_data(tiedoston_nimi: str) -> list:
    """ Lukee tiedoston sisällön ja muuntaa palauttaa listan, jossa on muutetut tietorivit
    Kutsuu funktiota muunna_tiedot, joka muuntaa tietorivin oikeisiin tietotyyppeihin.

    parametrit: tiedoston_nimi: käsiteltävän tiedoston nimi

    palauttaa: kulutustuotantotiedot: lista, jossa on muutetut tietorivit

    """
    kulutustuotantotiedot = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)  # Ohitetaan otsikkorivi
        for kulutustuotantotieto in f:
            kulutustuotantotieto = kulutustuotantotieto.strip()
            kulutustuotantotieto = kulutustuotantotieto.split(';')
            kulutustuotantotiedot.append(muunna_tiedot(kulutustuotantotieto))
    return kulutustuotantotiedot


def paivantiedot(paiva: date, kulutustuotantotiedot: list) -> list:
    """" laskee päivän kulutus- ja tuotantotiedot, muuntaa ne kilowattitunneiksi
    ja palauttaa ne listana

    parametrit:
    paiva: raportoitava päivä
    kulutustuotantotiedot: kulutus- ja tuotantotiedot sekä päivämäärät

    palauttaa: listan, jossa on päivän tiedot merkkijonoina
    """
    kulutus = [0, 0, 0]
    tuotanto = [0, 0, 0]
    for kulutustuotanto in kulutustuotantotiedot:
        if kulutustuotanto[0].date() == paiva:
            kulutus[0] += kulutustuotanto[1] / 1000
            kulutus[1] += kulutustuotanto[2] / 1000
            kulutus[2] += kulutustuotanto[3] / 1000
            tuotanto[0] += kulutustuotanto[4] / 1000
            tuotanto[1] += kulutustuotanto[5] / 1000
            tuotanto[2] += kulutustuotanto[6] / 1000
    return [
        f"{paiva.day}.{paiva.month}.{paiva.year}",
        f"{kulutus[0]:.2f}".replace(".", ","),
        f"{kulutus[1]:.2f}".replace(".", ","),
        f"{kulutus[2]:.2f}".replace(".", ","),
        f"{tuotanto[0]:.2f}".replace(".", ","),
        f"{tuotanto[1]:.2f}".replace(".", ","),
        f"{tuotanto[2]:.2f}".replace(".", ","),
    ]


def main():
    """ Pääohjelma  lukee datan lue data funktiolla
     laskee päivittäiset yhteenvedot kutsumalla paivantiedot funktiota
     Muodostaa kolme viikkoraportti (41,42,43) taulukkomuodossa
      Kirjoittaa raportit tiedostoon
       Ilmoittaa käyttäjälle, että raportti on tulostettu """
    viikon41_data = lue_data("viikko41.csv")
    viikon42_data = lue_data("viikko42.csv")
    viikon43_data = lue_data("viikko43.csv")
    # Viikko41
    viikko41 = "\nViikon 41 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko41 += "Päivä\t\tPvm\t\t\tKulutus [kWh]\t\t\tTuotanto [kWh]\n"
    viikko41 += "\t\t\t(pv.kk.vvvv) v1\t\t v2\t\t v3\t\t v1\t\t v2\t\t v3\n"
    viikko41 += "---------------------------------------------------------------------------\n"
    viikko41 += "Maanantai\t" + \
        "\t".join(paivantiedot(date(2025, 10, 6), viikon41_data)) + "\n"
    viikko41 += "Tiistai\t\t" + \
        "\t".join(paivantiedot(date(2025, 10, 7), viikon41_data)) + "\n"
    viikko41 += "Keskiviikko\t" + \
        "\t".join(paivantiedot(date(2025, 10, 8), viikon41_data)) + "\n"
    viikko41 += "Torstai\t\t" + \
        "\t".join(paivantiedot(date(2025, 10, 9), viikon41_data)) + "\n"
    viikko41 += "Perjantai\t" + \
        "\t".join(paivantiedot(date(2025, 10, 10), viikon41_data)) + "\n"
    viikko41 += "Lauantai\t" + \
        "\t".join(paivantiedot(date(2025, 10, 11), viikon41_data)) + "\n"
    viikko41 += "Sunnuntai\t" + \
        "\t".join(paivantiedot(date(2025, 10, 12), viikon41_data)) + "\n"
    # Viikko42
    viikko42 = "\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko42 += "Päivä\t\tPvm\t\t\tKulutus [kWh]\t\t\tTuotanto [kWh]\n"
    viikko42 += "\t\t\t(pv.kk.vvvv) v1\t\t v2\t\t v3\t\t v1\t\t v2\t\t v3\n"
    viikko42 += "---------------------------------------------------------------------------\n"
    viikko42 += "maanantai\t" + \
        "\t".join(paivantiedot(date(2025, 10, 13), viikon42_data)) + "\n"
    viikko42 += "Tiistai\t\t" + \
        "\t".join(paivantiedot(date(2025, 10, 14), viikon42_data)) + "\n"
    viikko42 += "Keskiviikko\t" + \
        "\t".join(paivantiedot(date(2025, 10, 15), viikon42_data)) + "\n"
    viikko42 += "Torstai\t\t" + \
        "\t".join(paivantiedot(date(2025, 10, 16), viikon42_data)) + "\n"
    viikko42 += "Perjantai\t" + \
        "\t".join(paivantiedot(date(2025, 10, 17), viikon42_data)) + "\n"
    viikko42 += "Lauantai\t" + \
        "\t".join(paivantiedot(date(2025, 10, 18), viikon42_data)) + "\n"
    viikko42 += "Sunnuntai\t" + \
        "\t".join(paivantiedot(date(2025, 10, 19), viikon42_data)) + "\n"
    # Viikko43
    viikko43 = "\nViikon 43 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko43 += "Päivä\t\tPvm\t\t\tKulutus [kWh]\t\t\tTuotanto [kWh]\n"
    viikko43 += "\t\t\t(pv.kk.vvvv) v1\t\t v2\t\t v3\t\t v1\t\t v2\t\t v3\n"
    viikko43 += "---------------------------------------------------------------------------\n"
    viikko43 += "Maanantai\t" + \
        "\t".join(paivantiedot(date(2025, 10, 20), viikon43_data)) + "\n"
    viikko43 += "Tiistai\t\t" + \
        "\t".join(paivantiedot(date(2025, 10, 21), viikon43_data)) + "\n"
    viikko43 += "Keskiviikko\t" + \
        "\t".join(paivantiedot(date(2025, 10, 22), viikon43_data)) + "\n"
    viikko43 += "Torstai\t\t" + \
        "\t".join(paivantiedot(date(2025, 10, 23), viikon43_data)) + "\n"
    viikko43 += "Perjantai\t" + \
        "\t".join(paivantiedot(date(2025, 10, 24), viikon43_data)) + "\n"
    viikko43 += "Lauantai\t" + \
        "\t".join(paivantiedot(date(2025, 10, 25), viikon43_data)) + "\n"
    viikko43 += "Sunnuntai\t" + \
        "\t".join(paivantiedot(date(2025, 10, 26), viikon43_data)) + "\n"
    with open("yhteenveto.txt", "w", encoding="utf-8") as f:
        f.write(viikko41)
        f.write(viikko42)
        f.write(viikko43)
    print("raportti kirjoitettu tiedostoon yhteenveto.txt")


if __name__ == "__main__":
    main()
