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


tekst="ala ma kota"
for i, litera in enumerate (tekst):
    print ( litera, end=':')


krotka=(1,2,3,1,1,1)
print(krotka.count(1))

krotka2=("Napis1", "Napis2", "Napis1", 1,2,3)
print(krotka2.index("Napis1"))
print(krotka2.count("Napis1"))

print(dir(tekst))
print (tekst.endswith("kota"))
print ("koty" in tekst)
print(tekst.capitalize())
print(tekst.title())


#slownik

#pusty słownik:
d=dict()
print(type(d))
d['a']=1
print(d)
d['b']=2
print(d)

print(dir(d))
print(d.keys())
print(d.values())
print(d.items())

slownik1={"aw":10,
          "bw":20}
slownik2=dict(a=1,b=2)

for k in slownik1:
    print(k)

slownik1.get('a') #nie ma takiego klkucza w słowniku
slownik1.get('a',0) # wyrzuci 0 bo nie ma a w słowniku
print(slownik1.get("aw"))


#zbiory
zbior={1,2,3,5}
zbior.add(4)
print(zbior)
print (len(zbior))
u=set([1,2,3])
w={2,3,4}
print(u-w)
print(u|w)
print(u&w)
print(u^w)