## Zad 1
#
# Napisz funkcję (lub funkcje), które zwrócą maksymalną spośród 3 liczb.
#
# W rozwiązaniu skorzystaj tylko z możliwośći definiowania funkcji i używania w nich operatorów porównania

def max_z_dwoch(a,b):
    if a>b:
        return a
    return b

def max_z_trzech(x,y,z):
    return max_z_dwoch(x, max_z_dwoch(y,z))

assert 0== max_z_trzech(0,0,0)
assert 3==max_z_trzech(1,2,3)
assert 10==max_z_trzech(10,2,-3)