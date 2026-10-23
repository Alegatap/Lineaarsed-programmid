from platform import java_ver
from random import randint
from math import *
from winreg import EnumValue
# Ülesanne 1
# print("Tere, maailm!")
# nimi=input("Mis teie nimi on? ")
# print(f"Tere, maailm! Tervistan sind {nimi}!")
# try:
#     vanus =int(input("Kui vana sa oled? "))
#     print(f"Tere, maailm! Tervistan sind {nimi}! Sa oled {vanus} aastat vana.")
# except ValueError:
#     print("Palun sisessta kektiv number vanuse jaoks.")

# Ülesanne 2
# vanus=18
# eesnimi="Jaak"
# pikkus=16.5
# kas_kaib_koolis=True
# print(f"vanus: {vanus}, tüüp on {type(vanus)},eesnimi: {eesnimi}, tüüp on {type(eesnimi)},pikkus: {pikkus}, tüüp on {type(pikkus)},kas_kaib_koolis: {kas_kaib_koolis}, tüüp on {type(kas_kaib_koolis)}")

# Ülesanne 3
# kommid=randint(1,100)
# print(f"laual on {kommid} kommid")
# try:
#     võtta=int(input("Kui valju sa tahad võtta ära? "))
#     kommid -= võtta
#     print(f"laual on nüüd {kommid} kommi")
# except ValueError:
#     print("Palun sisessta number")

# Ülesanne 4
# try:
#     C=float(input("Mis puu ümbermõõdu on? "))
#     d=round(C / pi, 1)
#     print(f"puu läbimõõdu on {d}")
# except ValueError:
#     print("Palun sisessta number")

# Ülesanne 5
# try:
#     M=float(input("Esimese külje pikkus: "))
#     N=float(input("Esimese külje pikkus: "))
#     diagonaal=round(sqrt(M**2+N**2),1)
#     print(f"diagonaal on {diagonaal}")
# except ValueError:
#     print("Sisessta numbrid")

#Ülesanne 6

# Leidke järgnevast näiteprogrammist loogiline viga:
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = aeg / teepikkus

# print("Sinu kiirus oli " + str(kiirus) + " km/h")

# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus =round(teepikkus / aeg,1) #kiirus on teepikkus / aeg
                                                
# print("Sinu kiirus oli ", float(kiirus), " km/h")  

#Ülesanne 7
#Koostada programm, mis arvutab aritmeetilise keskmise etteantud 5 täis arvust.
#Leia nende arvude summa, jagatuna kasutaja poolt sisestatud arvuga, täisarvuline osa ja jääk.
try:
    print("sisseta ainult täisarvud")
    Arv1=int(input("sissesta esimene arvud: "))
    Arv2=int(input("sissesta teine arvud: "))
    Arv3=int(input("sissesta kolmas arvud: "))
    Arv4=int(input("sissesta neljas arvud: "))
    Arv5=int(input("sissesta viies arvud: "))
    Jagatuna_arv=int(input("Mis arv sa tahad jagada meie arvude summa? "))
    Arv_sum=Arv1+Arv2+Arv3+Arv4+Arv5
    Arv_kesk=Arv_sum/5
    jag_arv=Arv_sum/Jagatuna_arv
    täis_osa=Arv_sum//Jagatuna_arv
    jääk=Arv_sum%Jagatuna_arv
    print(f"aritmeetilise keskmise on {Arv_kesk}")
    print(f"Summa on {Arv_sum}")
    print(f"Arv jagatud teie arvuga on {jag_arv}")
    print(f"täisarvuline osa on {täis_osa}")
    print(f"jääk osa on {jääk}")
except ValueError:
    print("sisseta ainult täisarvud")

# Joonista samasugune konn
#    @..@
#    (----)
#   ( \__/ )
# ^^ "" ^^  
print("\n"
      "\n @..@"
     "\n (----)"
    "\n ( \__/ )"
     "\n^^ "" ^^")