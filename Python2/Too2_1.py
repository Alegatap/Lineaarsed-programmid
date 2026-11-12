# 1. Juku
# Programm küsib eesnime. Kui nimi on Juku, kuvatakse „Lähme Jukuga kinno!“, muidu teatatakse, et täna kinno ei minda.
# Programm peab Juku ära tundma ka siis, kui nimi on kirjutatud suurtähtedega (JUKU) või väiketähtedega (juku).
# Kui nimi on kirjutatud ainult suurtähtedega, lisa märkus „Ära karju, Juku!“.

nimi=input("Sissesta teie nimi: ")
if nimi.lower() == "juku":
    print("Lähme Jukuga kinno!")
    if nimi.isupper():
        print("Ära karju, Juku!")
    try:
        vanus=int(input("Kui vana sa oled? "))
        if 0 <= vanus < 6:
            Pilet="tasuta"
        elif 6 <= vanus < 14:
            Pilet="Lastepilet"
        elif 15 <= vanus < 65:
            Pilet="täispilet"
        elif 65 <= vanus < 120:
            Pilet="Sooduspilet"
    except:
        print("Sissesta vanus numbriga!")
    try:
        print(f"Jutku vanus on {vanus} aastat, ta ostab {Pilet}")
    except:
       print("viga andmetes.")
else:
    print("täna kinno ei minda")
