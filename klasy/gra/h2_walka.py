import pytest
import random
from random import randint


class Przedmiot:
    def __init__(self, nazwa, bonus):
        self.nazwa = nazwa
        if isinstance(bonus, int):
            self.bonus_do_ataku = bonus
        else:
            raise ValueError("Bonus powinien być liczbą")


rufus = Postac("Rufus", 30, 100)
janusz = Postac("Janusz", 40, 100)
tulipan = Przedmiot("zielony tulipan zniszczenia", 5)
rufus.dodaj_przedmiot(tulipan)


def walka(atakujacy, broniacy):
    print(f"Walka {atakujacy.imie} vs {broniacy.imie}")
    print(atakujacy)
    print(broniacy)
    print("-" * 40)

    while atakujacy.zdrowie > 0 and broniacy.zdrowie > 0:
        moc_ataku_atakujacego = atakujacy.moc_ataku()
        print(f"{atakujacy.imie} uderza {broniacy.imie} z mocą {moc_ataku_atakujacego}")
        broniacy.otrzymaj_obrazenia(moc_ataku_atakujacego)

        if broniacy.zdrowie>0:
            moc_ataku_broniacego = broniacy.moc_ataku()
            print(f"{broniacy.imie} oddaje {atakujacy.imie} z mocą {moc_ataku_broniacego}")
            atakujacy.otrzymaj_obrazenia(moc_ataku_broniacego)

    print("Koniec walki")
    print(atakujacy)
    print(broniacy)

class Polozenie():
    def __init__(self, x, y, zasieg_x,zasieg_y):
        self.x=x
        self.y=y
        self.zasieg_x=zasieg_x
        self.zasieg_y = zasieg_y

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

    def s(self):
        self.y-=1
        if self.y<1:
            print ("Wyszedles poza planszę")
            exit()

    def a(self):
        self.x-=1
        if self.x<1:
            print ("Wyszedles poza planszę")
            exit()

    def w(self):
        self.y+=1
        if self.y>self.zasieg_y:
            print ("Wyszedles poza planszę")
            exit()

    def d(self):
        self.x+=1
        if self.x>self.zasieg_x:
            print ("Wyszedles poza planszę")
            exit()

    def __str__(self):
        return f"Położenie: x={self.x}, y={self.y}"

class Plansza:
    def __init__(self, gracz, wrog, skarb, x=10, y=10):
        self.gracz=gracz
        self.wrog=wrog
        self.skarb=skarb
        self.x=x
        self.y=y

        self.polozenie_gracza=Polozenie(randint(1, self.x),randint(1, self.y), self.x, self.y )
        self.polozenie_wroga = Polozenie(randint(1, self.x), randint(1, self.y), self.x, self.y)
        self.polozenie_skarbu = Polozenie(randint(1, self.x), randint(1, self.y), self.x, self.y)

    def ruch(self):
        print("Gracz:", self.polozenie_gracza)
        print("Wróg:", self.polozenie_wroga)
        print("Skarb:", self.polozenie_skarbu)

        kierunek = input("Podaj kierunek w-góra, s-dół, a-lewo, d-prawo: ")
        getattr(self.polozenie_gracza, kierunek)()

        if self.polozenie_gracza==self.polozenie_skarbu:
            print ("Otrzymałeś:", self.skarb)
            self.gracz.dodaj_przedmiot(self.skarb)
            self.polozenie_skarbu=Polozenie(-100, -100, self.x, self.y)

        if self.polozenie_gracza==self.polozenie_wroga:
            Postac.walka(self.gracz, self.wrog)
            if self.gracz.zdrowie<1:
                print ("Zginąłeś")
                exit ()
            else:
                print ("Dalej")


    def gra(self):
        while True:
            self.ruch()

noz = Przedmiot("Noz", 5)
plansza=Plansza(rufus, janusz, noz)
plansza.gra()

#walka(rufus, janusz)


def test_nowa_postac():
    postac = Postac("Albert", 1, 20)
    assert postac.imie == "Albert" and postac.atak == 1 and postac.zdrowie == 20 and postac.max_zdrowie == 20


def test_obrazenia():
    postac = Postac("Rafał", 5, 200)
    assert postac.zdrowie == 200
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.otrzymaj_obrazenia(200)
    assert postac.zdrowie == 0


def test_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(50)
    assert postac.zdrowie == 170


def test_leczenie_nieboszczyka():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(800)
    assert postac.zdrowie == 0
    postac.wylecz(50)
    assert postac.zdrowie == 0


def test_za_duze_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(500)
    assert postac.zdrowie == 200


def test_przedmiot():
    przedmiot = Przedmiot("Kula mocy", 10)
    assert przedmiot.nazwa == "Kula mocy"
    assert przedmiot.bonus_do_ataku == 10


def test_przedmiot_is_not_int():
    with pytest.raises(ValueError):
        Przedmiot("Kula mocy", "dziesięć")


def test_dodaj_przedmiot():
    postac = Postac("Rafał", 5, 200)
    przedmiot = Przedmiot("Rękawice grzmoty", 40)
    assert przedmiot not in postac.ekwipunek
    assert postac.atak == 5
    postac.dodaj_przedmiot(przedmiot)
    assert postac.atak == 45
    assert przedmiot in postac.ekwipunek


def test_zabierz_przedmiot():
    postac = Postac("Rafał", 5, 200)
    przedmiot = Przedmiot("Rękawice grzmoty", 40)
    postac.dodaj_przedmiot(przedmiot)
    postac.zabierz_przedmiot(przedmiot)
    assert przedmiot not in postac.ekwipunek


def test_postac_moc_ataku():
    postac = Postac("Rafał", 50, 200)
    assert postac.atak == 50
    moc_atak = postac.moc_ataku()
    assert (postac.atak // 2) <= moc_atak <= postac.atak


###########
# kruger = Postac("Freddie Kruger", 40, 200)
# kula = Przedmiot("Kula", 5)
# kruger.dodaj_przedmiot(kula)
# print(kruger)
