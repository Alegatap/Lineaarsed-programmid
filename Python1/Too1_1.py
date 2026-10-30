from platform import java_ver
from random import randint
from math import *
# Ülesanne 1
print("Tere, maailm!")
nimi=input("Mis teie nimi on? ")
print(f"Tere, maailm! Tervistan sind {nimi}!")
try:
    vanus =int(input("Kui vana sa oled? "))
    print(f"Tere, maailm! Tervistan sind {nimi}! Sa oled {vanus} aastat vana.")
except ValueError:
    print("Palun sisessta kektiv number vanuse jaoks.")

# Ülesanne 2
vanus=18
eesnimi="Jaak"
pikkus=16.5
kas_kaib_koolis=True
print(f"vanus: {vanus}, tüüp on {type(vanus)},eesnimi: {eesnimi}, tüüp on {type(eesnimi)},pikkus: {pikkus}, tüüp on {type(pikkus)},kas_kaib_koolis: {kas_kaib_koolis}, tüüp on {type(kas_kaib_koolis)}")


# Ülesanne 3
kommid=randint(1,100)
print(f"laual on {kommid} kommid")
try:
    võtta=int(input("Kui valju sa tahad võtta ära? "))
    kommid -= võtta
    print(f"laual on nüüd {kommid} kommi")
except ValueError:
    print("Palun sisessta number")

# Ülesanne 4
try:
    C=float(input("Mis puu ümbermõõdu on? "))
    d=round(C / pi, 1)
    print(f"puu läbimõõdu on {d}")
except ValueError:
    print("Palun sisessta number")

# Ülesanne 5
try:
    M=float(input("Esimese külje pikkus: "))
    N=float(input("Esimese külje pikkus: "))
    diagonaal=round(sqrt(M**2+N**2),1)
    print(f"diagonaal on {diagonaal}")
except ValueError:
    print("Sisessta numbrid")

#Ülesanne 6

# Leidke järgnevast näiteprogrammist loogiline viga:
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = aeg / teepikkus

# print("Sinu kiirus oli " + str(kiirus) + " km/h")
try:
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    kiirus = round(teepikkus / aeg, 1)  # kiirus on teepikkus / aeg
    print("Sinu kiirus oli ", float(kiirus), " km/h")
except ValueError:
    print("Palun sisessta kektiv number")
#Koostada programm, mis arvutab aritmeetilise keskmise etteantud 5 täis arvust.
#Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga, täisarvuline osa ja jääk.
try:
    print("sisseta ainult täisarvud")
    arv1=int(input("sissesta esimene arvud: "))
    arv2=int(input("sissesta teine arvud: "))
    arv3=int(input("sissesta kolmas arvud: "))
    arv4=int(input("sissesta neljas arvud: "))
    arv5=int(input("sissesta viies arvud: "))
    jagatuna_arv=int(input("mis arv sa tahad jagada meie arvude summa? "))
    arv_sum=arv1+arv2+arv3+arv4+arv5
    arv_kesk=arv_sum/5
    jag_arv=arv_sum/jagatuna_arv
    täis_osa=arv_sum//jagatuna_arv
    jääk=arv_sum%jagatuna_arv
    print(f"aritmeetilise keskmise on {arv_kesk}")
    print(f"summa on {arv_sum}")
    print(f"arv jagatud teie arvuga on {jag_arv}")
    print(f"täisarvuline osa on {täis_osa}")
    print(f"jääk osa on {jääk}")
except ValueError:
    print("sisseta ainult täisarvud")

#Ülesanne 8
# Joonista samasugune konn
#    @..@
#    (----)
#   ( \__/ )
# ^^ "" ^^  
print("\n"
      "\n @..@"
     "\n (----)"
    "\n ( \__/ )"
     "\n  ^^ "" ^^")

#Ülesanne 9
#Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c.
#Kasuta valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
try:
    a=float(input("Sisesta esimese külje pikkus: "))
    b=float(input("Sisesta teine külje pikkus: "))
    c=float(input("Sisesta kolmanda külje pikkus: "))
    P=a+b+c
    print(f"Kolmnurga ümbermõõdu on {P}")
except ValueError:
    print("Palun sisessta number")
#Ülesanne 10
# Pitsa
# Võtsite sõpradega (näiteks P inimest) suure pitsa, mille hind on 12,90 €.
# Jätate teenindajale 10% jootraha.
# Koosta programm, mis arvutab, kui palju igaüks peab maksma.
try:
    Hind=float(input("Kui palju pitsa maksab? "))
    inimesed=int(input("Mitu inimest on? "))
    peabmaksma=round(Hind*1.1/inimesed,2)
    print(f"Igaüks peab maksma {peabmaksma} €")
except:
    print("Palun sisessta number")