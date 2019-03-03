import re

pattern=re.compile("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]")

with open("python_chalange3.txt") as f:
    dane=f.read()

wynik=pattern.findall(dane)

print(wynik)
