import re


with open(r'C:\Users\kurs\workspace\input.txt') as fp:
    in_plik=fp.read()

print(re.findall(r'\d\d-\d\d\d', in_plik))
print(re.findall(r'\b\d\d-\d\d\d\b', in_plik)) #\b to boundry, wcześniej i później nie ma numerycnych znaków

print(re.findall(r'\d\d .{3} \d{4}', in_plik))
print(re.findall(r'\b\d{1,2}\s[A-Z][a-z]{2}\s\d{4}\b', in_plik))

print(re.findall(r'\S+@\S+', in_plik)) #* tzn 0 lub więcej razy, + tzn 1 lub więcej razy \S tzn dowolne znaki niespacjowe
print(re.findall(r'[\w\-+.]+@[\w\-.]{4,}', in_plik)) #[dowolne alfanumeryczne, minus, plus, kropka] conajmniej jeden raz występują, potem  @ i [dowolne alfanumeryczne, minus, kropka] ten nawias wystąpi od 4 razy wzwyż