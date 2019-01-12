liczby=[1,2,3,4]
liczby2=[5,6,7,8]

for i, l in enumerate(liczby):
    print(f"indeks={i}, wartość={l}")


def drukuj(lista):
    for i, l in enumerate(liczby):
        print(f"indeks={i}, wartość={l}")

drukuj(liczby)
drukuj(liczby2)


def potega (podstawa, wykladnik):
    return podstawa**wykladnik

print (potega(4,2))