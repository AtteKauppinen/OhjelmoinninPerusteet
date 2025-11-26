"""
Ohjelma joka tulostaa tiedostosta luettujen varausten alkiot ja niiden tietotyypit

varausId | nimi | sähköposti | puhelin | varauksenPvm | varauksenKlo | varauksenKesto | hinta | varausVahvistettu | varattuTila | varausLuotu
------------------------------------------------------------------------
201 | Muumi Muumilaakso | muumi@valkoinenlaakso.org | 0509876543 | 2025-11-12 | 09:00:00 | 2 | 18.50 | True | Metsätila 1 | 2025-08-12 14:33:20
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
202 | Niiskuneiti Muumilaakso | niisku@muumiglam.fi | 0451122334 | 2025-12-01 | 11:30:00 | 1 | 12.00 | False | Kukkahuone | 2025-09-03 09:12:48
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
203 | Pikku Myy Myrsky | myy@pikkuraivo.net | 0415566778 | 2025-10-22 | 15:45:00 | 3 | 27.90 | True | Punainen Huone | 2025-07-29 18:05:11
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
204 | Nipsu Rahapulainen | nipsu@rahahuolet.me | 0442233445 | 2025-09-18 | 13:00:00 | 4 | 39.95 | False | Varastotila N | 2025-08-01 10:59:02
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
205 | Hemuli Kasvikerääjä | hemuli@kasvikeraily.club | 0463344556 | 2025-11-05 | 08:15:00 | 2 | 19.95 | True | Kasvitutkimuslabra | 2025-10-09 16:41:55
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
"""
from datetime import datetime


def muunna_varaustiedot(varaus: list) -> list:
    # Tähän tulee siis varaus oletustietotyypeillä (str)
    # Varauksessa on 11 saraketta -> Lista -> Alkiot 0-10
    # Muuta tietotyypit haluamallasi tavalla -> Seuraavassa esimerkki ensimmäisestä alkioista
    muutettu_varaus = []
    muutettu_varaus.append(int(varaus[0]))
    muutettu_varaus.append(str(varaus[1]))
    muutettu_varaus.append(str(varaus[2]))
    muutettu_varaus.append(str(varaus[3]))
    muutettu_varaus.append(datetime.strptime(
        varaus[4], "%Y-%m-%d").date())
    aika_str = varaus[5].strip()
    if len(aika_str.split(':')) == 2:
        muutettu_varaus.append(datetime.strptime(aika_str, "%H:%M").time())
    else:
        muutettu_varaus.append(datetime.strptime(
            aika_str, "%H:%M:%S").time())
    muutettu_varaus.append(int(varaus[6]))
    muutettu_varaus.append(float(varaus[7]))
    muutettu_varaus.append(varaus[8].lower() == "true")
    muutettu_varaus.append(str(varaus[9]))
    muutettu_varaus.append(datetime.strptime(
        varaus[10], "%Y-%m-%d %H:%M:%S"))
    return muutettu_varaus


def hae_varaukset(varaustiedosto: str) -> list:
    # HUOM! Tälle funktioille ei tarvitse tehdä mitään!
    # Jos muutat, kommentoi miksi muutit
    varaukset = []
    varaukset.append(["varausId", "nimi", "sähköposti", "puhelin", "varauksenPvm", "varauksenKlo",
                     "varauksenKesto", "hinta", "varausVahvistettu", "varattuTila", "varausLuotu"])
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset


def vahvistetut_varaukset(varaukset: list):
    for varaus in varaukset[1:]:
        # - Nimi, Varattu tila, pv.kk.vvvv klo hh.mm
        if varaus[8]:  # Tulostetaan vain vahvistetut varaukset
            print(
                f"- {varaus[1]} {varaus[9]}, {varaus[4].strftime('%d.%m.%Y')}, klo {varaus[5].strftime('%H.%M')}")
    # lisätään tyhjä rivi lopuksi
    print()


def pitkät_varaukset(varaukset: list):
    for varaus in varaukset[1:]:
        # - Nimi, pv.kk.vvvv klo hh.mm, kesto X h, Varattu tila
        if varaus[6] >= 3:  # Tulostetaan vain varaukset, joiden kesto on 3 tai enemmän
            print(
                f"- {varaus[1]}, {varaus[4].strftime('%d.%m.%Y')}, klo {varaus[5].strftime('%H.%M')}, kesto {varaus[6]} h, {varaus[9]}")
    # lisätään tyhjä rivi lopuksi
    print()


def varauksen_vahvistusstatus(varaukset: list):
    for varaus in varaukset[1:]:
        # Nimi → Vahvistettu
        status = "Vahvistettu" if varaus[8] else "Ei vahvistettu"
        print(f" {varaus[1]} → {status}.")
    # lisätään tyhjä rivi lopuksi
    print()


def yhteenveto_vahvistuksista(varaukset: list):
    vahvistettu_count = sum(1 for varaus in varaukset[1:] if varaus[8])
    ei_vahvistettu_count = len(varaukset) - 1 - vahvistettu_count
    print(f"Vahvistettuja varauksia: {vahvistettu_count} kpl")
    print(f"Ei-vahvistettuja varauksia: {ei_vahvistettu_count} kpl")
    # lisätään tyhjä rivi lopuksi
    print()


def vahvistettujen_kokonaistulot(varaukset: list):
    kokonaistulot = sum(
        varaus[7] for varaus in varaukset[1:] if varaus[8])
    print(
        f"Vahvistettujen varausten kokonaistulot: {f'{kokonaistulot:.2f}'.replace('.', ',')} €")
    # lisätään tyhjä rivi lopuksi
    print()


def main():
    # HUOM! seuraaville riveille ei tarvitse tehdä mitään osassa A!
    # Osa B vaatii muutoksia -> Esim. tulostuksien (print-funktio) muuttamisen.
    # Kutsutaan funkioita hae_varaukset, joka palauttaa kaikki varaukset oikeilla tietotyypeillä
    varaukset = hae_varaukset("varaukset.txt")
    print("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)
    print("2) Pitkät varaukset(≥ 3 h)")
    pitkät_varaukset(varaukset)
    print("3) Varausten vahvistusstatus")
    varauksen_vahvistusstatus(varaukset)
    print("4) Yhteenveto vahvistuksista")
    yhteenveto_vahvistuksista(varaukset)
    print("5) Vavhistettujen varausten kokonaistulot")
    vahvistettujen_kokonaistulot(varaukset)


#    print(" | ".join(varaukset[0]))
#    print("------------------------------------------------------------------------")
#    for varaus in varaukset[1:]:
#        print(" | ".join(str(x) for x in varaus))
#        tietotyypit = [type(x).__name__ for x in varaus]
#        print(" | ".join(tietotyypit))
#        print("------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
