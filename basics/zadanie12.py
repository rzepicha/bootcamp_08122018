i = 0
while i < 101:
    if i%10==0:
        i += 1
        continue
    j = i ** 2
    print(j)
    i += 1

i=0
while i<101:
    if i%10 !=0:
        print(i**2)
    i+=1