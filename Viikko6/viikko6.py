# Copyright (c) 2025 Atte Kauppinen
# License: MIT

from datetime import datetime, date


def muunna_tiedot(data: list) -> list:
    """ Muuttaa tiedostossa annetut tietorivin tietotyypit oikeiksi tietotyypeiksi
    parametrit: 
    data: lista, jossa on 7 kenttää.
    Ensimmäinen kenttä on päivämäärä
    kentät 2-3 desimaalilukuja, kulutus ja tuotanto
    kenttä4 desimaaliluku lämpötila.

    palauttaa: lista, jossa on muutetut tietotyypit
    """
    muutettu_tietorivi = []
    muutettu_tietorivi.append(datetime.fromisoformat(data[0]))
    muutettu_tietorivi.append(float(data[1].replace(",", ".")))
    muutettu_tietorivi.append(float(data[2].replace(",", ".")))
    muutettu_tietorivi.append(float(data[3].replace(",", ".")))

    return muutettu_tietorivi


def lue_data(tiedoston_nimi: str) -> list:
    """ lukee tiedoston sisällön ja palauttaa rivit listana, jossa on muutetut tietotyypit

    Kutsuu funktiota muunna, jonka avulla funktio palauttaa listan,
      jossa on tietotyypit muutettu
      parametrit: tiedoston_nimi (str): ottaa vastaan tiedoston, jossa kentät on jaettu merkillä ;

      palauttaa: 
      dataa: lista, jossa on muutetut tietotyypit"""

    dataa = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)  # Ohitetaan otsikkorivi
        for data in f:
            data = data.strip()
            data = data.split(';')
            dataa.append(muunna_tiedot(data))
    return dataa


def aikavaliraportti(alku: date, loppu: date, dataa: list) -> str:
    """ 
    luo raportin aikaväliltä, lisäksi muuntaa annetut päivämäärät datetime.date muotoon

    parametrit:
    alku(date): alkupäivämäärä
    loppu(date): loppupäivämäärä
    dataa(list): sisältää kaiken datan.

    palauttaa:
    raportti(str): palauttaa luodun raportin merkkijonona
    """

    kulutus = 0
    tuotanto = 0
    lampotila = 0

    for paiva in dataa:

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


def luo_kuukausiraportti(kuukausi: int, dataa: list) -> str:
    """
    Luo kuukausiraportin

    parametrit:
    kuukausi(int): kuukausi, jolta raportti luodaan
    dataa(list): sisältää kaiken datan

    palauttaa:
    raportti(str): palauttaa luodun raportin merkkijonona
    """
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

    for paiva in dataa:
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
        f"{(lampotila/(paivien_lukumaara*24)):.2f}".replace(".", ",") + "°C\n"
    raportti += "\n"
    return raportti


def luo_vuosiraportti(dataa: list) -> str:
    """
    Luo vuosiraportin 2025

    parametrit:
    dataa(list): sisältää kaiken datan

    palauttaa:
    raportti(str): palauttaa luodun raportin merkkijonona
    """
    raportti = "\n"
    raportti += "Raportti vuodelta 2025\n"
    kulutus = 0
    tuotanto = 0
    lampotila = 0
    paivien_lukumaara = 0
    for paiva in dataa:
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
    """
    Kirjoittaa raportin tiedostoon raportti.txt.

    parametrit:
    raportti(str): raportti, joka kirjoitetaan tiedostoon
    """
    with open("raportti.txt", "w", encoding="utf-8") as f:
        f.write(raportti)


def main():
    """ 
    Pääohjelma ohjaa raportointohjelman toimintaa.
    Lukee datan tiedostosta, jonka jälkeen näyttää valikon käyttäjälle.
    Käyttäjä valitsee haluamansa raporttityypin ja ohjelma tulostaa raportin.
    Tulostuksen jälkeen käyttäjälle avautuu valikko, jossa hän voi valita
    haluaako hän kirjoittaa raportin tiedostoon, luoda uuden raportin vai lopettaa ohjelman.
    Ohjlema jatkaa toimintaansa, kunnes käyttäjä valitsee lopettaa ohjelman
    Ohjelmassa ei ole virheiden käsittelyä.
    """
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
                "Anna loppupäivämäärä muodossa pv.kk.vvvv: ")
            alku = datetime.strptime(alku, "%d.%m.%Y").date()
            loppu = datetime.strptime(loppu, "%d.%m.%Y").date()

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
