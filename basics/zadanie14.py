znalezione_maksimum = None
znalezione_minimum = None
#
# while True:
#     komenda = input("Podaj liczbę lub k by zakończyć: ")
#     if komenda == "k":
#         break
#     if komenda.isdigit():
#         liczba = int(komenda)
#         if znalezione_maksimum is None or liczba > znalezione_maksimum:
#             znalezione_maksimum = liczba
#         if znalezione_minimum is None or liczba < znalezione_minimum:
#             znalezione_minimum = liczba
#
#     else:
#         print("Nie podałeś liczby")
# print("znalezione max to: ", znalezione_maksimum)
# print("znalezione min to: ", znalezione_minimum)

while True:
    komenda = input("Podaj liczbę lub k by zakończyć: ")
    if komenda == "k":
        break
    if len(komenda)> 0 and komenda[0] == '-' and komenda[1:].isdigit():
        liczba = int(komenda[1:])
        liczba = -liczba
    elif komenda.isdigit():
        liczba = int(komenda)
    else:
        print("Nie podałeś liczby")

    if liczba or liczba==0:
        if znalezione_maksimum is None or liczba > znalezione_maksimum:
            znalezione_maksimum = liczba
        if znalezione_minimum is None or liczba < znalezione_minimum:
            znalezione_minimum = liczba

print("znalezione max to: ", znalezione_maksimum)
print("znalezione min to: ", znalezione_minimum)
