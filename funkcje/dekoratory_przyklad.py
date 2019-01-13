def loguj_uzycie(func):
    """
    to będzie dekorator . wypisze tekst przed i po uruchomieniu funkcji
    :param pobierz_dane:
    :return:
    """

    def wrapper(*args, **kwargs):
        print("To się wykona przed")

        #print("To sie wykona po")
        return f"Wynik: {func(*args, **kwargs)}"
    return wrapper

@loguj_uzycie
def potega (podstawa, wykladnik):
    wynik=podstawa**wykladnik
    return wynik

def pobierz_dane():
    print("Pobralem dane")

# print("Bez dekoracji")
# pobierz_dane()
#
# print("Udekorowane")
# pobierz_dane=loguj_uzycie(pobierz_dane)
# pobierz_dane()

print(potega(2,4))