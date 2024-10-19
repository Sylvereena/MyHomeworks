initial_list = [10, 20, 10, 20, 30, 40, 30, 50]
unique_list = []
for item in initial_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
