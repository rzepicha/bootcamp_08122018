class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko

    def przedstaw_sie(self):
        print(f'Czesc jestem {self.imie} {self.nazwisko}')


class Pracownik(Osoba):

    def pracuj(self):
        print("Pracuje")
    def __init__(self, imie, nazwisko, stanowisko):
         Osoba.__init__(self,imie, nazwisko)
         #super().__init__(imie, nazwisko) #to samo co linijka wyżej
         self.stanowisko=stanowisko

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f'pracuje jako {self.stanowisko}')

class Informatyk(Pracownik):
    def programuj(self):
        print ("...programuje")


osoba=Osoba("Adam", "Słodowy")
osoba.przedstaw_sie()

pracownik=Informatyk("Rafał", "Korzeniowski", "trener")
pracownik.przedstaw_sie()
pracownik.pracuj()
