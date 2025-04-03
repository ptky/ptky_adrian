#Hetessy Adrián

import random

def elvalaszto(hossz, char):
    return hossz * char


def lec(szel, szov):
    print(elvalaszto(szel * 2, "*"))
    print(f"*{szov:^{(szel - 1) * 2}}*")
    print(elvalaszto(szel * 2, "*"))

def tetelek(tetelek, szel):
    ar_vegso = 0
    for tetel in tetelek:
        ar = random.randint(200, 6000)
        ar_vegso += ar
        ar_str = str(ar) + ' Ft'
        print(f"{tetel:<{szel}}{ar_str:>{szel}}")
    print(elvalaszto(szel * 2, "="))
    return ar_vegso


def ossz_koltseg(ossz, szel):
    print(f"{'Összesen: ':<{szel}}{str(ossz) + ' Ft':>{szel}}")
    print(f"{'Szervizdij: ':<{szel}}{str(ossz) + ' Ft':>{szel}}")
    print(elvalaszto(szel * 2, "="))


def fizetendo(ar, szel):
    print(f"{'Fizetendő: ':<{szel}}{str(ar) + ' Ft':>{szel}}")


def alairas(szel):
    prefix = szel + round(szel * (1/2))
    print(f"\n{'_'*round(szel/4):<{szel}}{'_'*round(szel/4):>{szel}}")
    print(f"{'Dátum':^{round(szel/4)}}{' ' * prefix}{'Cég':^{round(szel/4)}}")


tetelek_szama = int(input("Add meg a számlád tételeinek számát itt: "))
szamla_szel = int(input("Add meg számlád szélességét itt: "))

def main(szel, tet_szam):
    tetelek_j = [f'tétel{i + 1}' for i in range(tet_szam)]
    lec(szel, "NYUGTA")
    ar_ossz = tetelek(tetelek_j, szel)
    ossz_koltseg(ar_ossz, szel)
    fizetendo(ar_ossz + round(ar_ossz/10), szel)
    alairas(szel)
    lec(szel, "CÉG")


main(szamla_szel, tetelek_szama)
