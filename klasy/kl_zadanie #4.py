#klasa do 2 opcji
class BasketEntry:
    def __init__(self,produkt, ilosc):
        self.produkt=produkt
        self.ilosc=ilosc

    def count_price(self):
        return self.produkt.cena*self.ilosc
#klasa do 2 opcji


class Basket:
    def __init__(self):
        self.entries=[]


    def add_produkt(self,produkt,ilosc):
        #1opcja z uzyciem listy
        # add=True
        # for position in self.entries:
        #     if position[0]==produkt:
        #         position[1]+=ilosc
        #         add=False
        # if add:
        #         self.entries.append([produkt, ilosc])
        #
        # def count_total_price(self): #to powinno być 1 wcięcie mniej, na wysokości def adda-produkt
        #     total = 0
        #     for e in self.entries:
        #         pr = e[0]
        #         total += pr.price * e[1]
        #     return total

        #1 opcja

        #2 opcja z uzyciem nowej klasy
        basket_entry=BasketEntry(produkt, ilosc)
        for be in self.entries:
            if be.produkt==produkt:
                be.ilosc+=ilosc
                break
        else:
            self.entries.append(basket_entry)

    def count_total_price(self):
        total = 0
        for e in self.entries:
            total += e.count_price()
        return total
        #2opcja

    def generate_report(self):
        report="Produkty w koszyku: \n"
        for e in self.entries:
            report += f'-{e.produkt.nazwa}({e.produkt.id}), cena: {e.produkt.cena} x {e.ilosc} \n'
        report+= f"W sumie: {self.count_total_price()}"
        return report


class Produkt:
    def __init__(self, nazwa, id, cena):
        self.nazwa=nazwa
        self.id=id
        self.cena=cena





def test_basket_init():
    basket=Basket()
    assert basket.entries==[]

def test_produkt_init():
    produkt=Produkt("woda",1, 10)
    assert produkt.nazwa=="woda"
    assert produkt.cena==10
    assert produkt.id==1

def test_basket_add_product_twice():
    basket=Basket()
    produkt=Produkt("woda",1, 10)
    basket.add_produkt(produkt, 5)
    basket.add_produkt(produkt, 3)
    assert len(basket.entries)==1

def test_basket_count_total_prce():
    basket=Basket()
    produkt=Produkt("woda",1, 10)
    basket.add_produkt(produkt, 5)
    basket.add_produkt(produkt, 3)
    assert len(basket.entries)==1

def test_basket_generate_report():
    basket = Basket()
    produkt = Produkt("woda", 1, 10.0)
    basket.add_produkt(produkt, 5)
    assert basket.generate_report()=="""Produkty w koszyku:
-woda(1), cena: 10.0 x 5
W sumie: 50.0"""
