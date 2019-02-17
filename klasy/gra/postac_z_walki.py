
class Postac:
    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self._atak = atak
        self.max_zdrowie = zdrowie
        self.zdrowie = zdrowie
        self.ekwipunek = []

    def dodaj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def zabierz_przedmiot(self, przedmiot):
        self.ekwipunek.remove(przedmiot)

    def moc_ataku(self):
        return random.randint(self.atak // 2, self.atak)

    def __str__(self):
        napis = f"""Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.
EKWPIUNEK:
"""
        for przedmiot in self.ekwipunek:
            napis += f"{przedmiot.nazwa},{przedmiot.bonus_do_ataku} do ataku"
        return napis

    @property
    def atak(self):
        return self._atak + sum([e.bonus_do_ataku for e in self.ekwipunek])

        # 2 opcja
        # bonusy=0
        # for przedmiot in self.ekwipunek:
        #     bonusy+= przedmiot.bonus_do_ataku
        # return self._atak+bonusy

    def otrzymaj_obrazenia(self, obrazenia):
        print(f"{self.imie} oberwał za {obrazenia} obrażeń")
        self.zdrowie -= obrazenia
        if self.zdrowie < 0:
            self.zdrowie = 0


    def wylecz(self, pkt_zdrowia):
        if self.zdrowie == 0:
            return False
        self.zdrowie += pkt_zdrowia
        if self.zdrowie > self.max_zdrowie:
            self.zdrowie = self.max_zdrowie

