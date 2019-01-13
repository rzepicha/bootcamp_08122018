
def splaszcz(lista):
    lista2 = []
    for el in lista:
        if isinstance(el, list):
            for i in splaszcz(el):
                lista2.append(i)
        else:
            lista2.append(el)
    return lista2


def test_spłaszcz_pusta_lista():
    assert splaszcz([])==[]

def test_splaszcz_plaska_lista():
    assert splaszcz ([1,2,3])== [1,2,3]

def test_splaszcz_zagniezdzona_lista():
    assert splaszcz([1, 2, [3,4]])==[1,2,3,4]
    assert splaszcz([1,2,3,[4,5,[6]],7])== [1,2,3,4,5,6,7]
