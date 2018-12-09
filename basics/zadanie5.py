miastoA=input("Podaj nazwę miasta A: ")
miastoB=input("Podaj nazwę miasta B: ")
dystans=input("Podaj liczbę km: ")
cena=input("Podaj cenę paliwa: ")
spalanie=input("Podaj spalanie samochodu na 100km: ")

cena=float(cena)
spalanie=float(spalanie)
dystans=float(dystans)

koszt=((dystans*spalanie)/100)*cena

druk=f"""Koszt przejazdu {miastoA}-{miastoB} to {koszt} PLN"""

print (druk)