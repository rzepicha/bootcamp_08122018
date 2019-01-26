## Zad 2
# Napisz funkcję, która:

# 1. Jeśli jej argument będzie listą, tuplą bądź zbiroem, zwróci sumę jej elementów

# 2. Jeśli jej argument będzie słownikiem, zwróci sumę wartości

# W obu przypadkach ignoruj napisy - o ile napisy nie reprezentują liczb

def sumuj(obiekt):
    wynik = 0
    if isinstance(obiekt, dict):
        obiekt=obiekt.values()
    for x in obiekt:
        try:
            x=int(x)
            wynik+=x
        except ValueError:
            pass
    return wynik

assert sumuj([1,2,3])==6
assert sumuj([10,20,30])==60
assert sumuj([1,2,'a',3])==6
assert sumuj([1,2,'4',3])==10
assert sumuj({'a':10,1:20,'c':30,'d':'40'})==100