# Copyright (c) 2025 Atte Kauppinen
# License: MIT
"""Sähkönkulutuksen ja -tuotannon käsittelyä viikolta 42 CSV-tiedostosta ja sen tulostus konsoliin."""
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
    """ laskee päivän kulutus- ja tuotantotiedot, muuntaa ne kilowattitunneiksi
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
    """ Pääohjelma lukee datan, 
    laskee päivän yhteenvedon ja 
    tulostaa viikon 42 raportin konsoliin """

    tiedot = lue_data("viikko42.csv")
    print("\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä\t\tPvm\t\tKulutus [kWh]\t\tTuotanto [kWh]")
    print("\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\tv2\tv3")
    print("---------------------------------------------------------------------------")
    print("maanantai\t" + "\t".join(paivantiedot(date(2025, 10, 13), tiedot)))
    print("Tiistai\t\t" + "\t".join(paivantiedot(date(2025, 10, 14), tiedot)))
    print("Keskiviikko\t" + "\t".join(paivantiedot(date(2025, 10, 15), tiedot)))
    print("Torstai\t\t" + "\t".join(paivantiedot(date(2025, 10, 16), tiedot)))
    print("Perjantai\t" + "\t".join(paivantiedot(date(2025, 10, 17), tiedot)))
    print("Lauantai\t" + "\t".join(paivantiedot(date(2025, 10, 18), tiedot)))
    print("Sunnuntai\t" + "\t".join(paivantiedot(date(2025, 10, 19), tiedot)))


if __name__ == "__main__":
    main()
