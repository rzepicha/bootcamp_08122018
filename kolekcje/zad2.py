liczby=[]
i=0
while len(liczby)<10:
    liczba=input("Podaj liczby lub 'k' by zakończyć:")
    if liczba =='k':
        break
    liczba=int(liczba)

    liczby.append(liczba)
    i+=1
print (liczby)
sr=sum(liczby)/len(liczby)
print(f"Średnia: {sr}")



#wersja2
dane=input("Podaj liczby, rozdziel je spacjami: ")
dane=dane.split()
print(dane)
dane2=[]
for d in dane:
    dane2.append(int(d))
print(dane2)

#albo wyrażenie listowe
dane=[int(d) for d in dane]
print(dane)

#albo mapowaniem
dane=map(int,dane)
print(list(dane))