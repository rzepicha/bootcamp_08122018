# produkty={'kapusta':1,
#           'pomidory':8,
#           'jabłka':2}
#
# co=input("Wybierz 1 produkt: kapusta, pomidory, jabłka: ")
# ile=input("Podaj ilość w kg:")
#
# for warzywo in produkty:
#     if co==warzywo:
#         a=produkty.get(co)
#         print(a*eval(ile))


#rozwiązanie Rafała
prod={'kapusta':1,
          'pomidory':8,
          'jabłka':2}

magazyn={'kapusta':10,
          'pomidory':10,
          'jabłka':10}

while True:
    rola = input("Czy jesteś [klient]em [k], czy [dostawca] [d], [q] by zakończyć?")
    if rola.lower() in ['klient', 'k']:

        while True:
            print("Nasz sklep oferuje: ")
            for produkt, cena in prod.items():
                print(f'-{produkt}-{cena:.2f}')

            zakup = input("co kupujesz? [k] by zakończyć")
            if zakup.lower() == 'k':
                print("zapraszamy ponownie")
                break
            waga = float(input(f"ile chcesz kupić - [{zakup}]"))
            if waga > magazyn[zakup]:
                print("Nie ma tyle w magazynie")
                print(f'W magazynie pozostało: {magazyn[zakup]}')
            else:
                cena = prod.get(zakup)
                if cena:
                    koszt = waga * prod[zakup]
                    print(f"Za [{zakup}] zapłacisz: {koszt:.2f}")
                    magazyn[zakup] = magazyn[zakup] - waga
                    print(f'W magazynie pozostało: {magazyn[zakup]}')

                else:
                    print("To nie jest produkt z listy")

    elif rola.lower() in ['dostawca', 'd']:
        # ścieżka dostawcy
        # dodanie produktu - 'd'
        # zmiana ceny - 'z'
        # prosimy o podanie produktu w ormacie nazwa ilosc cena
        while True:
            do_dodania=input("Podaj produkt w formacie [nazwa ilosc cena]: ")
            if len(do_dodania.split())==3:
                nazwa, ilosc, cena = do_dodania.split()
                ilosc=float(ilosc)
                cena=float(cena)
                prod[nazwa] = cena
                break
            else:
                print ("zły format")
        if nazwa in magazyn:
            magazyn[nazwa] = magazyn.get(nazwa, 0) + ilosc
            print(nazwa, ilosc, cena, sep="\t")

            print("Dziękuję, produkt dodany")
    elif rola.lower()=='q':
        print("Koniec")
        break
