print("     ", end="")

for poz in range(10):
    print(f"{poz:5}", end="")
print()
print()

for poziom in range (0,10):
    print(f"{poziom:5}", end="")

    for pion in range (0,10):
        print(f"{poziom*pion:5}", end="")

    print()



