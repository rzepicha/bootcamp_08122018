def wiecej_niz(tekst, x):
    zbior = set()
    unikalne=set(tekst)
    for i in unikalne:
        if tekst.count(i)>x:
            zbior.add(i)
    return zbior
    print(zbior)

    #return {i for i in set(tekst) if tekst.count(i)>x} #2. wersja

def test_wiecej_niz():
    assert wiecej_niz ('ala ma kota a kot ma ale',3)=={'a', ' '}

