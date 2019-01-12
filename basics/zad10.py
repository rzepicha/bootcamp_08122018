napis=input("Podaj swój napis: ")

zlicz={}
for znak in napis:
    if znak in zlicz:
        zlicz[znak]+=1
    else:
        zlicz[znak]=1
    #zlicz[znak]=zlicz.get(znak,0)+1 # drugi sposób zamiast pętli if-else


for z, c in zlicz.items():
    print (f"litery {z}, ilosc {c}")