import random

nyugta_szel = 15

def elvalaszto(hossz):
    return hossz * "*"


def lec(szel, szov):
    print(elvalaszto(szel))
    print(f"*{szov:^{szel - 2}}*")
    print(elvalaszto(szel))

def tetelek(tetelek, szel):
    for tetel in tetelek:
        ar = random.randint(200, 6000)
        ar_str = str(ar) + ' Ft'
        print(f"{tetel:<{szel}}{ar_str:>{szel}}")

tetelek_j = [f'tétel{i + 1}' for i in range(10)]

tetelek(tetelek_j, nyugta_szel)