#przykłady input

# x=int(input("Podaj wartość x: "))
# y=int(input("Podaj y: "))
# print (x+y)
#
# i=0
# while True:
#     print (i)
#     i+=1
#     if i == 100:
#         break


tekst="Ala ma kota"
for i, litera in enumerate (tekst):
    print (i, litera)


krotka=(1,2,3,1,1,1)
print(krotka.count(1))

krotka2=("Napis1", "Napis2", "Napis1", 1,2,3)
print(krotka2.index("Napis1"))
print(krotka2.count("Napis1"))
