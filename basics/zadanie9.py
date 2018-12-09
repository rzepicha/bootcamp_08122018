import datetime

rok = int(input("Podaj rok urodzenia: "))

if rok > 2000:
    print("Nie jesteś pełnoletni")
else:
    print("Jesteś pełnoletni!")

y = datetime.datetime.now().year

if y - rok >= 18:
    print("Jesteś pełnoletni!")
else:
    print("Nie jesteś pełnoletni")
