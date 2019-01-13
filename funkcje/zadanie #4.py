
def formatuj (*napisy, **zmienne):
    napis="\n".join(napisy)
    for zmienna in zmienne:
        napis = napis.replace(f"${zmienna}",zmienne[zmienna])

    return napis


def test_formatuj_napis_bez_znacznikow():
    assert formatuj("Hello world")== "Hello world"

def test_formatuj_wiele_napisow_bez_znacznikow():
   assert formatuj("Hello world", "Hi !") == "Hello world \n Hi !"

def test_formatuj_napis_bez_znacznikow_ale_ze_zmiennymi_jako_argument():
    assert formatuj ("Hello world", name="john", lastname="kowalski") == "Hello world"

def test_formatuj_napis_ze_zmienna():
    assert formatuj ("Hello $name", name="John")== "Hello John"
    assert formatuj("Hello $name $lastname", name="john", lastname="kowalski") == "Hello john kowalski"