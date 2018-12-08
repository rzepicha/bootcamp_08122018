dl = float(input("Podaj długość opakowania: "))
szer = float(input("Podaj szerokość opakowania: "))
wys = float(input("Podaj wysokość opakowania: "))

objet = dl * szer * wys

print("Objętość wynosi:", objet)
print("Czy objętość większa niż 1000 cm3?: ", objet > 1000)

print (f"Objętość wynosi: {objet}")
print (f"Czy objętość większa od 1 litra?: {objet>1000}")
print()
print()
print("z ifem:")

if objet > 1000:
    print("Objętość jest większa niż 1000 cm3")
else:
    print("Objętość jest mniejsza niż 1000 cm3")
