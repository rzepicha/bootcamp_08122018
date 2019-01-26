## Zad 6
#Napisz funkcję, które sprawdzi, czy zadana liczba jest doskonała

def liczba_doskonala(liczba):
    """
    pomysły na optymalizację:
    1. sprawdzenie dzielenia tylko do n/2
    2. jeśli coś nie jest podzielne przez 2 to nie będzie przez liczbę parzystą
    3. jeśli coś jest nieparzyste to nie będzie doskonałe
    """

    total=0
    for a in range (1, liczba):
        if liczba%a==0:
            total+=a
    return total==liczba


assert liczba_doskonala(6)==True
assert liczba_doskonala(7)==False
assert liczba_doskonala(28)==True
assert liczba_doskonala(496)==True