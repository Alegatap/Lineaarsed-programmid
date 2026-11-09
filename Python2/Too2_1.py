try:
    x = int(input("sissesta arv: "))
    if x > 0:
        print("Positiivne arv")
        print("See rida on ka if-i sees")
    print("See rida täidetakse alati")
except:
    print("sissesta täisarv")

####################################################################

try:
    x = int(input("Sisesta arv: "))
    if x == 1:
        print("Õige")
    else:
        print("Vale")
except:
        print("sissesta täisarv")

####################################################################

vastus = input("Kas soovid jätkata? (jah/ei) ")
print("sinu vastus oli: ",vastus)
# vastustype=type(vastus)
# print("sinu tüüp on: ",vastustype)
# vastus_on_tekst=vastus.isalpha()
# print("kas see on tekst?",vastus_on_tekst)
if vastus.isalpha():
    if vastus.lower() == "jah":
        print("Jätkame!")
    else:
        print("Head aega!")
else:
    print("Palun sisesta jah või ei")
    
####################################################################

try:
    x = int(input("Sisesta arv -5 kuni 5: "))
    if x < -5:
        print("Vähe")
    elif -5 <= x <= 5:
        print("OK")
    else:
        print("Palju")
except:
    print("sissesta täisarv")

####################################################################

nimi = input("Sisesta nimi: ")
print("Ainult tähed:", nimi.isalpha())
print("Suurtähtedega:", nimi.isupper())
print("Algab suurtähega:", nimi.istitle())
if nimi.isalpha() and nimi.istitle():
    print("Nimi sobib.")
    try:
        vanus = int(input(f"Tere, {nimi}! Kui vana sa oled?: "))
        if vanus >= 18:
            juhiluba = input("Kas sul on juhiluba? (jah/ei) ")
            if juhiluba.lower() == "jah":
                print("Võid autot juhtida.")
            else:
                print("Kõigepealt tee juhiload.")
        else:
            print("Oled autojuhtimiseks liiga noor.")
    except:
        print("sissesta teie vanus arvutega")
else:
    print("Nimes tohib olla ainult tähti!")

