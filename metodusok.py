def csillag(hossz):
    i = 0
    while i < hossz:
        print("*", end="")
        i+=1
    print()  
    
def vonal(hossz):
    i = 0
    while i < hossz:
        print("-", end="")
        i+=1
    print()        

def nyugta():
    csillag(24)
    print("*", f"{"NYUGTA":^20}", f"{"*":>1}")
    csillag(24)    

def tetelek(elso="jani", masodik="pisti", harmadik="bozótnéni"):
    import random
    asdk = random.randint(30,1500)
    ijgwi = random.randint(30,1500)
    űwekj = random.randint(30,1500)

    tetel1 = f"{elso:<16} {asdk:<4} {'Ft':>2}"
    tetel2 = f"{masodik:<16} {ijgwi:<4} {'Ft':>2}"
    tetel3 = f"{harmadik:<16} {űwekj:<4} {'Ft':>2}"
    
    print(tetel1)
    print(tetel2)
    print(tetel3)
 
def osszesen():
    osszesen = f"{'Ft':>2}"
    szervizdij = f"{'Ft':>2}"
    
def ossz():
    nyugta()
    tetelek()
    vonal(24)
    vonal(24)
    osszesen()
    
ossz()
