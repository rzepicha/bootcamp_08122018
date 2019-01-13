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
#######################

def zsumuj(lista):
    return sum(lista)

print(zsumuj([10,20,30]))



def zsumuj2(a,b,*args):
    print(args)
    print(type(args))
    return sum(args)
print (zsumuj2('a','b', 10,20, 50, 100))


def wykonaj_operacje(operacja,*args):
    print(args)
    print(type(args))
    return operacja(args)
print (wykonaj_operacje(min, 10,20, 50, 100)) #argumenty pozycyjne args - mogę dowolną liczbę argumentów przekazac
print (wykonaj_operacje(sum, 10,20, 50, 100))




