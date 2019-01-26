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


## Zad 7
# Napisz dekorator, który będzie printował w konsoli czas wykonania dekorowanej
import time

def czas_wykonania(dekorowana_funkcja):
    def wrapper (*args, **kwargs):
        start=time.time()
        wynik=dekorowana_funkcja(*args, **kwargs)
        stop=time.time()
        print(f"Czas wykonania funkcji {dekorowana_funkcja.__name__} z argumentami {args},{kwargs} wynosi {stop-start} sek")
        return wynik
    return wrapper

liczba_doskonala=czas_wykonania(liczba_doskonala)
liczba_doskonala(1000000)