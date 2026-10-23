print("Tere, maailm!")
nimi=input("Mis teie nimi on? ")
print(f"Tere, maailm! Tervistan sind {nimi}!")
try:
    vanus =int(input("Kui vana sa oled? "))
    print(f"Tere, maailm! Tervistan sind {nimi}! Sa oled {vanus} aastat vana.")
except ValueError:
    print("Palun sisessta kektiv number vanuse jaoks.")
