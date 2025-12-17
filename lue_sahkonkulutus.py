# Copyright (c) 2025 Atte Kauppinen
# License: MIT
"""Sähkönkulutuksen ja -tuotannon käsittelyä viikolta 42 CSV-tiedostosta ja sen tulostus konsoliin."""
from collections import defaultdict
from datetime import datetime
import locale
try:
    locale.setlocale(locale.LC_TIME, "fi_FI.UTF-8")
except locale.Error:
    pass


def muunna_tiedot(kulutustuotanto: list) -> list:
    """ Muuttaa tiedot oikeisiin tietotyyppeihin"""
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
    """ Lukee sähkönkulutus- ja tuotanto tiedoston (viikko42.csv) ja palauttaa listan, jossa on muutetut tietorivit """
    kulutustuotantotiedot = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)  # Ohitetaan otsikkorivi
        for kulutustuotantotieto in f:
            kulutustuotantotieto = kulutustuotantotieto.strip()
            kulutustuotantotieto = kulutustuotantotieto.split(';')
            kulutustuotantotiedot.append(muunna_tiedot(kulutustuotantotieto))
    return kulutustuotantotiedot


def ryhmittele_paivittain(tiedot: list) -> dict:
    """ Ryhmittelee tunnit päivittäin ja laskee summat vaiheittain """
    paivittain = defaultdict(
        lambda: [0, 0, 0, 0, 0, 0])  # 3 kulutusta + 3 tuotantoa

    for rivi in tiedot:
        pvm = rivi[0].date()  # otetaan vain päivämäärä datetime-oliosta
        for i in range(6):    # kulutus ja tuotanto
            paivittain[pvm][i] += rivi[i+1]

    return paivittain


def taulukon_tulostus(paivittain: dict):
    """Tulostaa tiedot taulukkona"""
    print("Viikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n")
    print(f"{'Päivä':<12}{'Pvm':<11}{'Kulutus (kWh)':<30}{'Tuotanto (kWh)':<30}")
    print(f"{'':<12}{'(pv.kk.vvvv)':<15}{'v1      v2      v3':<30}{' v1     v2     v3':<30}")
    print("-" * 80)
    for pvm in sorted(paivittain.keys()):
        paiva_nimi = pvm.strftime("%A")  # viikonpäivä suomeksi
        pvm_str = pvm.strftime("%d.%m.%Y")  # esim. 13.10.2025
        kulutus = " ".join([f"{x/1000:.2f}".replace('.', ',').rjust(7)
                            for x in paivittain[pvm][0:3]])
        tuotanto = " ".join([f"{x/1000:.2f}".replace('.', ',').rjust(7)
                            for x in paivittain[pvm][3:]])
        print(f"{paiva_nimi:<12}{pvm_str:<12}{kulutus:<30}{tuotanto:<30}")


def main():
    """ Pääohjelma ajaa sähkönkulutuksen ja -tuotannon käsittelyn viikolta 42 """
    tiedot = lue_data("viikko42.csv")
    paivittain = ryhmittele_paivittain(tiedot)
    taulukon_tulostus(paivittain)


if __name__ == "__main__":
    main()
