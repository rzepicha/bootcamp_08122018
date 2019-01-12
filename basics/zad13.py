print([i/10 for i in range (0,11)])

print({(i, i**2, i**3) for i in range (-10,11)})

napisy={"Ala ma kota", "kot ma alę", "kotek"}
print({x: len(x) for x in napisy})
