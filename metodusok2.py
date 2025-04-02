#Hetessy Adrián

import random

nyugta_szel = 100

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

tetelek_j = [f'tétel{i + 1}' for i in range(10)]

def main(szel):
    lec(szel, "NYUGTA")
    tetelek(tetelek_j, szel)

main(nyugta_szel)
