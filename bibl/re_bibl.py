#wyrazenia regularne
# https://docs.python.org/3.7/library/re.html?highlight=re#module-re
import re

s="Ala ma kota! Kot ma Ale. Kot lubi mleko. Nie lubi ryb."

print(re.findall('lubi', s))
print(re.findall('lubi .', s))#kropka to dowolny znak * to dowolna ilość razy
print(re.findall('... ma', s))

print(re.findall(r'.{3} ma', s)) #łapie każde "ma" i 3 dowolne znaki wcześniej
print(re.findall(r'\w{3} ma', s))
print(re.findall(r'\w*', s))
print(re.findall(r'\w+', s))
print(re.findall(r'[A-Z]',s))
print(re.findall(r'[A-Z].*?\.',s)) #*?bierze jak najmniej ale zeby spełnić regułę
print(re.findall(r'[A-Z].*\.',s)) #* bierze dowolną ilość znaków, jak najwięcej
print(re.findall(r'[A-Z].*?[\.\!]',s)) # całe zdnaie nie tylko do kropki ale i do wykszyknika

print(re.findall(r'([A-Z].\w*)\W.*?[\.\!]',s)) #\s to wszystki białe znaki \w znaki alfanumeryczne