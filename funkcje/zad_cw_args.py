
def napisy (*args):
    """napisz funkcje, która przyjmie dowolną liczbę napisów,
    1. zwróci te napisy połączone znakiem nowej linii
    >>> napisy('a','b')
    a
    b
    """
    return "\n".join(args)
print(napisy("ala", "ma"))



def napisy2 (*args, funkcja=None):
    tekst="\n".join(args)
    if funkcja:
        tekst=funkcja(tekst)
    return tekst
print(napisy2("ala", "ma"))

def upper(napis2):
    return napis2.upper()

print(napisy2("albo","nie", "ma", funkcja=upper))
print(napisy2("albo","nie", "ma", funkcja=str.upper))

#############


def napisy3 (*args, **kwargs):
    tekst="\n".join(args)
    for k in kwargs:
        tekst=kwargs[k](tekst)
    return tekst
print(napisy3("ala", "ma", "kot", funkcja2=str.upper, funkcja3=str.title))

