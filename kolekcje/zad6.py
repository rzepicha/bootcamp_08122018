liczby = [5, 2, 1, 4, 3]
print(liczby)

index_min, index_max = None, None

for index in range(len(liczby)):
    if index_min is None or liczby[index] < liczby[index_min]:
        index_min = index
    if index_max is None or liczby[index] > liczby[index_max]:
        index_max = index

liczby[index_max], liczby[index_min] = liczby[index_min], liczby[index_max]

assert liczby == [1, 2, 5, 4, 3]

print(liczby)
