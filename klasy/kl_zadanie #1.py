class Produkt:
    """Opis produktów"""
    def __init__(self, nazwa, id, cena):
        self.nazwa=nazwa
        self.id=id
        self.cena=cena



    def print_info(self):
        """wypisanie info o produkcie"""
        print(f'Produkt {self.nazwa}, id: {self.id}, cena: {self.cena} PLN')

    def __str__(self):
        return f'Produkt: {self.nazwa}, id: {self.id}, cena: {self.cena} PLN'

produkt=Produkt(1, "woda", 2.99)
produkt.print_info()

print(produkt)
print(help(produkt))