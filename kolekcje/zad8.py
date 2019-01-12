#inny sposób
tekst1="Ala ma kota"
tekst2="Ala<ma>kota"
tekst3="Ala <>ma kota"
tekst4=input("Podaj tekst:")

dlugosc=0

for znak in tekst1:
    pass

assert dlugosc==0
print(dlugosc==0)

#tu będą błędy:
# for znak in tekst2:
#     pass
#
# assert dlugosc==2
# print(dlugosc==2)

dlugosc=0
licz=False
for znak in tekst4:
    if znak=="<":
        licz=True
    elif znak==">":
        licz=False
        break
    elif licz:
        dlugosc +=1

print(dlugosc)