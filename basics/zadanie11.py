x=int(input("Podaj pozycję gracza X: "))
y=int(input("Podaj pozycję gracza Y: "))

if x<=10:
    if y<=10:
        print("Pozycja gracza: lewy dolny róg")
    elif y>10 and y<=90:
        print("Pozycja gracza: lewa krawędź")
    elif y>90 and y<=100:
        print("Pozycja gracza: lewy górny róg")
    else:
        print ("Gracz poza planszą")
elif x>10 and x<=90:
    if y<=10:
        print("Pozycja gracza: dolna krawędź")
    elif y>10 and y<=90:
        print("Pozycja gracza: centrum")
    elif y>90 and y<=100:
        print("Pozycja gracza: górna krawędź")
    else:
        print ("Gracz poza planszą")
elif x>90 and x<=100:
    if y<=10:
        print("Pozycja gracza: prawy dolny róg")
    elif y>10 and y<=90:
        print("Pozycja gracza: prawa krawędź")
    elif y>90 and y<=100:
        print("Pozycja gracza: prawy górny róg")
    else:
        print ("Gracz poza planszą")
else:
    print ("Gracz poza planszą")