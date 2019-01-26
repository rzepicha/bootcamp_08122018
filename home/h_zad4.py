## zad 4
#Napisz funkcję, które wypisze n pierwszych wierszy trójkąta Pascala


def trojkat_pascala(n):
    a=[[1]]
    i=1

    for i in range(1,n):
        a.append([1])
        for j in range(1,i):
            a[i].append(a[i-1][j-1]+a[i-1][j])
        a[i].append(1)
    return a

def print_pascal(a):
    n = len(a)
    for i, row in enumerate(a):
        print(" "*(n-i), end="")
        for col in row:
            print (f'{col:4}', end="")
        print ()


a=trojkat_pascala(10)
print_pascal(a)

##########
#def trojkat_pascala2(n):
#    return (11**i for i in range(n))
#    #działa tylko do n=7
#print(list(trojkat_pascala2(5)))
###########

assert[[1]]==trojkat_pascala(1)
assert[[1], [1,1]]==trojkat_pascala(2)
assert[[1],[1,1],[1,2,1],[1,3,3,1]]==trojkat_pascala(4)
