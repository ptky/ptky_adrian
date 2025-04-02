import random

def csillag(hossz):
    i = 0
    while i < hossz:
        print("*", end="")
        i += 1
    print()

def egyenlo(hossz):
    i = 0
    while i < hossz:
        print("=", end="")
        i += 1
    print()

def nyugta():
    csillag(24)
    print("*", f"{'NYUGTA':^20}", "*")
    csillag(24)

def tetelek(elso="jani", masodik="pisti", harmadik="bozótnéni"):
    asdk = random.randint(30, 1500)
    ijgwi = random.randint(30, 1500)
    awekj = random.randint(30, 1500)
    
    dfjsdjfidsjf = asdk + ijgwi + awekj

    tetel1 = f"{elso:<16} {asdk:<4} {'Ft':>2}"
    tetel2 = f"{masodik:<16} {ijgwi:<4} {'Ft':>2}"
    tetel3 = f"{harmadik:<16} {awekj:<4} {'Ft':>2}"
    
    print(tetel1)
    print(tetel2)
    print(tetel3)
    
    return dfjsdjfidsjf

def osszesen2(osszesen):
    szervizdij = osszesen * 0.1
    print(f"{"Összesen:":<16} {osszesen:<4} Ft")
    print(f"{"Szervizdíj:":<15} {szervizdij:<4.1f} Ft")


def ossz():
    nyugta()
    osszeg = tetelek()
    egyenlo(24)
    osszesen2(osszeg)
    egyenlo(24)

ossz()
