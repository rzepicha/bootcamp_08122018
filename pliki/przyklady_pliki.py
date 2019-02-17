with open ("readme.txt", encoding="UTF-8") as f: #defaultowo jest 'r' read
    for line in f:
        print(len(line))

with open("readme3.txt", 'w') as f: # 'w' write
    f.write("Ala ma kota,")

with open("readme3.txt", 'a') as f: #'a' od append,  jest trybem dołączającym, gdyby było znowu 'w' to by się nadpisał plik
    f.write(" kot ma ale")



# with open ("readme.txt") as f:
#     print (f.read())


