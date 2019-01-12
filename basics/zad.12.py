lista=[9,1,6,8,4,3,2,0]

for i in range(len(lista)):
    index_minim = i
    for j in range(i, len(lista)):
        if lista[j]< lista[index_minim]:
            index_minim = j
            #print("nowe minimum to: ", lista[i])
            #print("nowy index_minimum to: ", i)

    lista[i], lista[index_minim]=lista[index_minim], lista[i]
print(lista)


#wyrażenie listowe
x=[1,2,3,6]
print([i**2 if i%2==0 else i for i in x])

