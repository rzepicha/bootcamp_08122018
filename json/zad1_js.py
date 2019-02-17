import json
import getpass

# w bazie:imie, nazwisko, email, rok ur, pensja
try:
    with open("employees.json") as fp:
        pracownicy = json.load(fp)
except FileNotFoundError:
    pracownicy2 = []

#pracownicy2 = []


def dodaj_pracownika(pracownicy2):
    imie = input("Dodaj imie: ")
    nazwisko = input("Dodaj nazwisko: ")
    email = input("Dodaj email: ")
    rok_ur = input("Dodaj rok urodzenia: ")
    pensja = input("Dodaj pensję: ")

    pracownik = {"imie": imie,
                 "nazwisko": nazwisko,
                 "rok urodzenia": rok_ur,
                 "pensja": pensja}

    pracownicy2.append(pracownik)

    with open ("employess.json", 'w') as fp:
        json.dump(pracownicy2, fp)


def wypisz_pracownika(pracownicy2):
    for nr, pracownik in enumerate(pracownicy2, start=1):
        print(f"-[{nr}] {pracownik['imie']} {pracownik['nazwisko']} - rok: {pracownik['rok_ur']}, "
              f"{pracownik['pensja']} PLN")

def usun_pracownika(pracownicy2):
    nr=input("Którego pracownika usunąć?: ")
    # haslo=getpass.getpass("Podaj hasło: ")
    # if haslo!= 'TAJNE':
    #     print('zle haslo')
    #     return

    del pracownicy2[int(nr)-1]

    with open ("employess.json", 'w') as fp:
        json.dump(pracownicy2, fp)



wybierz = input("Co chcesz zrobic? [d-dodaj, w-wypisz]: ")
if wybierz == 'd':
    dodaj_pracownika(pracownicy2)
elif wybierz == 'w':
    wypisz_pracownika(pracownicy2)
elif wybierz == 'u':
    usun_pracownika(pracownicy2)
#
# pracownik={}
# pracownicy=[]
#
#
# pyt=input("Co chcesz zrobic? [d-dodaj, w-wypisz]: ")
#
# if pyt =='d':
#     pracownik['Imie']= input("Dodaj imie: ")
#     pracownik['Nazwisko'] = input("Dodaj nazwisko: ")
#     pracownik['email'] = input("Dodaj email: ")
#     pracownik['Rok urodzenia'] = input("Dodaj rok urodzenia: ")
#     pracownik['pensja'] = input("Dodaj pensję: ")
#     pracownicy.append(pracownik)
#     print(pracownicy)
#
# with open ("employess2.json", 'w') as fp:
#     json.dump(pracownicy, fp)
