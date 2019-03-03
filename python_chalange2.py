from string import ascii_letters

with open("pyth_chalenge2.txt") as f:
    dane=f.read()
out=[]

for d in dane:
    if d in ascii_letters:
        out.append(d)

import re

pattern=re.compile("[a-zA-Z]")
print(pattern.findall(dane))

print(out)
print("".join(out))


print(ord('a'))
print(chr(97))