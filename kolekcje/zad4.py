podzielne=[]
i=0

for liczba in range (0,101):
    if liczba%3==0 or liczba%5==0:
        podzielne.append(liczba)
        i+=1

print(f"Lista liczb podzielnych przez 3 i 5: {podzielne}, jest tych liczb {i}")


#wersja2
lista=[liczba for liczba in range (0,101) if liczba%3==0 or liczba%5==0]
print (len(lista))
print("\n".join(map(str, lista)))