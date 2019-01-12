
liczby=set()
parzyste=set(range(0,100,2))
while True:
    komenda= input("Podaj liczbę lub k by zakończyc ")
    if komenda == 'k':
        break
    else:
        liczby.add(int(komenda))


print("licz unikalnych jest: ", len(liczby))
print("z tego parzystych: ", len (liczby & parzyste))