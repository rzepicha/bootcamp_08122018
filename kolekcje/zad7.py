napis=input("Podaj swój napis:")
nap=napis.lower()

samogloski=["e","i","o","u","y","a"]
samog="aeiouy"

i=0
for litera in nap:
    if litera in samog:
        i=i+1
print(i)


