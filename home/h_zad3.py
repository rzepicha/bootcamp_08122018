## Zad 3

#Napisz funkcję, która sprawdzi czy podany napis jest palindromem


def czy_palindrom(tekst):
    tekst="".join(tekst.lower().split())
    lewy = 0
    prawy = len(tekst) - 1
    while prawy>=lewy:
        if not tekst[lewy]==tekst[prawy]:
            return False
        lewy+=1
        prawy-=1
    return True


assert czy_palindrom("Kobyła ma mały bok") == True
assert czy_palindrom("Zakopane na pokaz") == True
assert czy_palindrom("Ala ma kota") == False



def czy_palindrom2(tekst):
    tekst = "".join(tekst.lower().split())
    return tekst==tekst[::-1]