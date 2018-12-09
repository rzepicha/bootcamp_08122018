a=int(input("Podaj liczbę a: "))
b=int(input("Podaj liczbę b: "))
operator=input("Podaj operatora: ")

if operator=="+":
    print("Wynik: ", a+b)
elif operator=="-":
    print("Wynik: ", a-b)
elif operator=="*":
    print("Wynik: ", a*b)
elif operator=="/":
    print("Wynik: ", a/b)
else:
    print("Błąd operatora")

print (eval(f"{a} {operator}{b}"))