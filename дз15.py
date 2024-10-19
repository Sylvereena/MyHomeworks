kort1 = (1, 2, 3, 4, 5)
kort2 = (3, 4, 5, 6, 7)
kort3 = (4, 5, 8, 9)

common_elements = set(kort1) & set(kort2) & set(kort3)
result = tuple(common_elements)

print("Элементы, которые есть во всех кортежах:", result)