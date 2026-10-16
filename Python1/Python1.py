#print("Hello, \nWorld")
#print("Tere Tulemast\t!")
#print("Õpin",1, ".kursusel")
#print("Õpin",1, ".kursusel",sep="***")
#print("2026", "10", "01", sep="-")
#print("Sama ", end="")
#print("rida")

#nimi= "Python"
#print("See on", nimi)
#kursus = int(1)
#print("Õpin",kursus, ".kursusel")

#nimi=input("sisesta oma nimi: ")
#print("See on", nimi)
#kursus = int(input("mis kursus sa õpib?"))
#print("Õpin",kursus, ".kursusel")

# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a, "+", b, "=",a + b)

# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a, "-", b, "=",a - b)

# print("jagamine")
# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a, "/", b, "=",a / b,"\n", round(a / b,2))

# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a, "//", b, "=",a // b)

# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a, "**", b, "=",a ** b)

# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(a, "%", b, "=",a % b)

# a = float(input("Esimene arv: "))
# b = float(input("Teine arv: "))
# print(f"{a} * {b} =", a * b)
a = float(input("Esimene arv: "))
b = float(input("Teine arv: "))
tehe=input("Tehe: ")
print(f"{a}{tehe}{b} = {eval(f"{a} {tehe} {b}")}")
