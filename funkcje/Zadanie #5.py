import pytest

def silnia(liczba):
    if liczba<0:
        raise ValueError("Argument musi być >=0")
    if liczba==0:
        return 1
    else:
        return liczba*silnia(liczba-1)


def test_silnia_dla_0():
    assert silnia(0)==1

def test_silnia_dla_wieksze_od_0():
    assert silnia(3)==6
    assert silnia(5) == 120

def test_silnia_dla_mniejsze_od_0():
    with pytest.raises(ValueError) as e:
        silnia (-10)

#
# def dodaj(cyfry):
#     if cyfry==0:
#         return 0
#     else:
#         return cyfry+dodaj(cyfry-1)
#
# print(dodaj(5))