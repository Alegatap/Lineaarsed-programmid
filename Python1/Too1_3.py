from datetime import *
import calendar
from math import *
# Ülesanne 1
# Kirjuta programm, mis sind tervitab ja kuvab ekraanile tänane kuupäev moduli datetime kasutades ja date.today() funktsiooni abil.
# from datetime import *
# tana=date.today()
# print(f"Täna on {tana}")

# Kasuta erinevate formaatide kuvamiseks ekraanile järgmised funktsioonid:
# # 27/12/2022
# tana = tana.strftime("%d/%m/%Y")
# # December 27, 2022
# tana = tana.strftime("%B %d, %Y")
# # 12/27/22
# tana = tana.strftime("%m/%d/%y")
# # Dec-27-2022
# tana = tana.strftime("%b-%d-%Y")
# Omadused day, month, year kasutatakse päeva, kuu ja aasta parameetri leidmiseks date klassist.
# Arvuta mitu päeva on jäänud kuu lõpuni, aasta lõpuni.
# Arvuta oma vanus aastates, kuudes ja päevades. {}
try:
    tana=date.today()
    tana1=tana.strftime("%d/%m/%Y")
    print(f"Täna on {tana1}")
    tana2=tana.strftime("%B.%d.%Y")
    print(f"Täna on {tana2}")
    tana3=tana.strftime("%m/%d/%y")
    print(f"Täna on {tana3}")
    month=calendar.monthrange(2026, 11)[1]
    newyear=date(2027,1,1)
    print(f"kuu lõpuni on {month-tana.month} päeva, aasta lõpuni on {(newyear-tana).days} päeva")
    sünnipäev=date(2003,11,9)
    vanus=(tana-sünnipäev).days
    print(f"sa oled {vanus} päeva vana või {vanus/365.25} aastat või {int(vanus/12)} kuud")
except ValueError:
    print("unlucky")
# Ülesanne 2
# Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
# +Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
# +Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.

print(3 + 8 / (4 - 2) * 4)

# Ülesanne 3
# Ruudu sees asub ring. Ringi raadius on R.
# Leia ja väljasta ekraanile ruudu pindala, ruudu ümbermõõt, ringi pindala, ringi ümbermõõt.

R=float(input("sissesta R: "))
D=2*R
ümbermõõt1=D*4
pindala1=D**2
ümbermõõt2=pi*D
pindala2=pi*R**2
print(f"ruudu pindala on {pindala1}, ruudu ümbermõõt on {ümbermõõt1}, ringi pindala on {ümbermõõt2}, ringi ümbermõõt on {pindala2}")
# Ülesanne 4
# Koosta programm, mis arvutab välja Maa ümbermõõdu ekvaatori kohal 2-eurostes müntides ehk teisisõnu:
#  kui palju 2-euroseid münte tuleb panna üksteise kõrvale, et rida ulatuks ümber Maa. Kasuta teadmist, et Maa raadius ekvaatori kohal on 6378 km.
# Algandmed (Maa raadius, mündi läbimõõt jne) omista programmi alguses sisukate nimedega muutujatele.
# Kuna ümbermõõdu arvutamiseks tuleb kasutada  PI-d (3,14...), siis võid selle (umbkaudse) väärtuse otse programmi kirjutada.  
# Püüdke välja mõelda viise, kuidas juhuslikest vigadest valemis hoiduda (teisendamised, ümardamise täpsus jne). Võimalusel võrrelge tulemusi teistega. Kui on erinevusi, leidke ühiselt põhjused.
# Kas programm on piisavalt hästi kirjutatud, et algandmete muutumise korral (näiteks juhul, kui on vaja arvutada Marsi ümbermõõtu 1-eurostes müntides) on parandusi selge ja lihtne teha?
EuroDiameter=0.00002575
MaaDiameter=6378*2
MaaÜmbermõõdu=pi*MaaDiameter
EuroMaaDiameter=MaaÜmbermõõdu/EuroDiameter
print(f"Meil on vaja {int(EuroMaaDiameter)} 2-euroseid münte")

# Ülesanne 5
# Eelnevaid teadmisi kasutades kirjuta programm, mis väljastaks:
# kill-koll kill-koll killadi-koll kill-koll kill-koll killadi-koll kill-koll kill-koll kill-koll
# kill-koll

# Saab kasutada muutujaid. Kuva iga sõna suure tähega.

# Ülesanne 6
# Koosta programm, mis väljastaks järgmised laulusõnad suurte tähtedega:

# Rong see sõitis tsuhh tsuhh tsuhh,
# piilupart oli rongijuht.
# Rattad tegid rat tat taa,
# rat tat taa ja tat tat taa.
# Aga seal rongi peal,
# kas sa tead, kes olid seal?

# Rong see sõitis tuut tuut tuut,
# piilupart oli rongijuht.
# Rattad tegid kill koll koll,
# kill koll koll ja kill koll kill.



# ....Sisend, väljund, tingimus....

# Ülesanne 7

# Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile ristküliku ümbermõõdu ja pindala.
 
# Ülesanne 8
# Kütusekulu arvutamine

#     Kasutaja sisestab tangitud kütuse liitrid
#     Kasutaja sisestab läbitud kilomeetrid
#     Programm leiab kütusekulu 100km kohta keskmiselt
 
# Ülesanne 9
# Rulluisutajad

#     Rulluisutaja keskmine kiirus on 29,9km/h
#     Kui kaugele jõuab M minutiga
 
# Ülesanne 10
# Ajateisendus

#     Kasutaja sisestab aja minutites
#     Sinu valem leiab ja väljastab tunnid ja minutid
#     Näiteks: sisestus 72, vastus 1:12