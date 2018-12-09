calkowite=[100,2,-20,-90,3,0,1,2,5,-9]

dodatnie=0
ujemne=0
zero=0

for el in calkowite:
    if el>0:
        dodatnie+=1
    elif el<0:
        ujemne+=1
    else:
        zero+=1


print (f"Dodatnie: {dodatnie}")
print (f"Ujemne: {ujemne}")
print (f"Zera: {zero}")


#wersja2
dodatnie2=[el for el in calkowite if el>0]
ujemne2=[el for el in calkowite if el<0]

licznik_dodatnich=len(dodatnie2)
licznik_ujemne=len(ujemne2)

print (f"Dodatnie2: {licznik_dodatnich}")
print (f"Ujemne2: {licznik_ujemne}")