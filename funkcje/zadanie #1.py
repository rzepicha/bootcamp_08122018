def czy_jest_pierwsza(a):
    for i in range (2,a//2+1):
        if a%i==0:
            return False
    return True
print(czy_jest_pierwsza(113))

#assert czy_jest_pierwsza(17)==True #assert czy jest pierwsza (17)
#assert czy_jest_pierwsza(10)==False #assert not czy jest pierwsza (10)