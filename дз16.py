kort1 = (1, 2, 3, 4, 5)
kort2 = (3, 4, 5, 6, 7)
kort3 = (4, 5, 8, 9)

set1 = set(kort1)
set2 = set(kort2)
set3 = set(kort3)
unique_elements = (set1 | set2 | set3) - (set1 & set2 & set3)

result = tuple(unique_elements)

print("Элементы, уникальные для каждого кортежа:", result)