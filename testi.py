# Copyright (c) 2025 Atte Kauppinen
# License: MIT

from datetime import datetime


def muunna_tiedot(tietue: list) -> list:

    return [
        datetime.fromisoformat(tietue[0]),
        float(tietue[1].replace(",", ".")),
        float(tietue[2].replace(",", ".")),
        float(tietue[3].replace(",", ".")),
    ]


def lue_data(tiedoston_nimi: str) -> list:
    tietokanta = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)  # Otetaan kenttien esittelytiedot pois
        for tietue in f:
            tietue = tietue.split(";")
            tietokanta.append(muunna_tiedot(tietue))

    return tietokanta


def aikavaliraportti(alku: datetime.date, loppu: datetime.date, tietokanta: list) -> str:
    """ Tulostaa raporttiin aikaväliltä:
    -alku- ja loppupäivä
    kokonaiskulutus aikaväliltä
    kokonaistuotanto aikaväliltä
    keskilämpötila aikaväliltä"""

    kulutus = 0
    tuotanto = 0
    lampotila = 0
    alku = datetime.strptime(alku, "%d.%m.%Y").date()
    loppu = datetime.strptime(loppu, "%d.%m.%Y").date()

    for paiva in tietokanta:

        if alku <= paiva[0].date() <= loppu:
            kulutus += paiva[1]
            tuotanto += paiva[2]
            lampotila += paiva[3]
    raportti = "\n"
    raportti += f"Raportti aikaväliltä {alku.day}.{alku.month}.{alku.year} - "
    raportti += f"{loppu.day}.{loppu.month}.{loppu.year}\n"
    raportti += "kokonaiskulutus: " + \
        f"{kulutus:.2f}".replace(".", ",") + "kWh\n"
    raportti += "kokonaistuotanto: " + \
        f"{tuotanto:.2f}".replace(".", ",") + "kWh\n"
    raportti += "keskilämpötila: " + \
        f"{(lampotila/((loppu-alku).days*24)):.2f}".replace(".", ",") + "°C\n"
    raportti += "\n"
    return raportti


def luo_kuukausiraportti(kuukausi: int, tietokanta: list) -> str:
    """Muodostaa kuukausikohtaisen yhteenvedon valitulle kuukaudelle."""
    kuukaudet = [
        "Tammikuu",
        "Helmikuu",
        "Maaliskuu",
        "Huhtikuu",
        "Toukokuu",
        "Kesäkuu",
        "Heinäkuu",
        "Elokuu",
        "Syyskuu",
        "Lokakuu",
        "Marraskuu",
        "Joulukuu"]
    raportti = "\n"
    raportti += f"raportti kuukaudelta: {kuukaudet[kuukausi-1]}"
    kulutus = 0
    tuotanto = 0
    lampotila = 0
    paivien_lukumaara = 0

    for paiva in tietokanta:
        if paiva[0].date().month == kuukausi:
            kulutus += paiva[1]
            tuotanto += paiva[2]
            lampotila += paiva[3]
            paivien_lukumaara += 1
    raportti += "kokonaiskulutus on: " f"{kulutus:.2f}".replace(
        ".", ",") + "kWh\n"
    raportti += "kokonasituotanto on: " f"{tuotanto:.2f}".replace(
        ".", ",") + "kWh\n"
    raportti += "keskilämpötila on: " + \
        f"{(lampotila/(paivien_lukumaara*24))}".replace(".", ",") + "°C\n"
    raportti += "\n"
    return raportti


def luo_vuosiraportti(tietokanta: list) -> str:
    """Muodostaa koko vuoden yhteenvedon."""
    raportti = "\n"
    raportti += "Raportti vuodelta 2025\n"
    kulutus = 0
    tuotanto = 0
    lampotila = 0
    paivien_lukumaara = 0
    for paiva in tietokanta:
        kulutus += paiva[1]
        tuotanto += paiva[2]
        lampotila += paiva[3]
        paivien_lukumaara += 1
    raportti += "kokonaiskulutus on: " f"{kulutus:.2f}".replace(
        ".", ",") + "kWh\n"
    raportti += "kokonasituotanto on: " f"{tuotanto:.2f}".replace(
        ".", ",") + "kWh\n"
    raportti += "keskilämpötila on: " + \
        f"{(lampotila/(paivien_lukumaara*24)):.2f}".replace(".", ",") + "°C\n"
    raportti += "\n"
    return raportti


def kirjoita_raportti_tiedostoon(raportti: str):
    """Kirjoittaa raportin rivit tiedostoon raportti.txt."""
    with open("raportti.txt", "w", encoding="utf-8") as f:
        f.write(raportti)


def main():
    tiedostondata = lue_data("2025.csv")
    while True:
        print("\n")
        print("Valitse Raporttityyppi:")
        print("1) Päiväkohtainen yhteenveto aikaväliltä")
        print("2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle")
        print("3) Vuoden 2025 kokonaisyhteenveto")
        print("4) Lopeta ohjelma")
        valinta1 = int(input("Valitse haluamasi vaihtoehto numerolla 1-4: "))
        if valinta1 == 1:
            alku = input(
                "Anna alkupäivämäärä muodossa pv.kk.vvvv: ")
            loppu = input(
                "Anna alkupäivämäärä muodossa pv.kk.vvvv: ")
            raportti = aikavaliraportti(alku, loppu, tiedostondata)
            print(raportti)
        elif valinta1 == 2:
            kuukausi = int(input("Anna kuukausi numero (1-12): "))
            raportti = luo_kuukausiraportti(kuukausi, tiedostondata)
            print(raportti)
        elif valinta1 == 3:
            raportti = luo_vuosiraportti(tiedostondata)
            print(raportti)
        elif valinta1 == 4:
            print("lopetetaan ohjelma")
            break
        else:
            continue
        print("Mitä haluat tehdä seuraavaksi?")
        print("1) Kirjoita raportti tiedostoon raportti.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta)")
        valinta2 = int(input("Valitse haluamasi vaihtoehto numerolla 1-3: "))
        if valinta2 == 1:
            kirjoita_raportti_tiedostoon(raportti)
            print("raportti kirjoitettu tiedostoon\n")
        elif valinta2 == 2:
            print("\n")
            continue
        elif valinta2 == 3:
            break


if __name__ == "__main__":
    main()
