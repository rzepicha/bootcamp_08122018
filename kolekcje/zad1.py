tupla=(1,3,5,2,7,4,8,9,6,10)

print(tupla[1])
print(tupla[-2])
print(tupla[2:8])
print(tupla[0:10:3])
print(tupla[-2::-2])
print(tupla[::-2])


lista=[1,2,3,4,5]
lista.append("AA")
lista.append(['a','b'])
lista.extend(['c','d'])
print(lista)
print(lista[-1][-1])

print("Jak działa pop:")
print(lista)
print(lista.pop())
print(lista)

lista2=[1,2,9,6,8]
print(lista2)
print("sortowanie")
print(lista2.sort())
print(lista2)

lista3=[3,1,8]
print(lista3)
print(sorted(lista3))
print(lista3)