
def policz_znaki(napis1, start="<", stop=">"):
    #licz=False
    wynik=0
    poziom=0
    for i in napis1:
        if i == start:
            #licz=True
            poziom+=1
        elif i == stop:
            #licz=False
            poziom-=1
        elif poziom: #elif licz:
            #wynik+=1
            wynik+=poziom
    return wynik



def test_policz_znaki_1_poziom_zagn ():
    assert policz_znaki ('ala ma <kota> a kot ma ale')== 4
    assert policz_znaki('ala ma <kota> a kot <ma> ale') == 6

def test_policz_znaki_1_poziom_zagn_inne_nawiasy ():
    assert policz_znaki('ala ma [kota] a kot [ma] ale', '[',']') == 6

def test_policz_znaki_2_poziom_zagn ():
    assert policz_znaki ('ala ma <<kota>> a kot <ma> ale')== 10



def test_policz_znaki_w_pustym_napisie():
    assert policz_znaki("")==0

def test_policz_znaki_w_niepustym_napisie_bez_nawiasow():
    assert policz_znaki("ala ma kota")==0
