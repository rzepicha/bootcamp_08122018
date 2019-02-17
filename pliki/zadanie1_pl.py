import sys

f_name=None
if len(sys.argv)>1:
    f_name=sys.argv[1]


if f_name:
    with open (f_name, encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            print (f"{i}: {line}", end="")
else:
    print("Nie podałeś nazwy pliku")

    

#2 wersja
import sys

# try:
#     f_name = None
# except IndexError:
#     print("Nie podałeś nazwy pliku")
#     exit()
#
#
# try:
#     with open(f_name, encoding="utf-8") as f:
#         for i, line in enumerate(f, start=1):
#             print(f"{i}: {line}", end="")
# except FileNotFoundError:
#     print("Nie ma takiego pliku")


