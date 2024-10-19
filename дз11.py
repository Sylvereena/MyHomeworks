import random

list = [random.randint(-20, 50) for _ in range(12)]

min = min(list)
max = max(list)

negatives = sum(1 for i in list if i < 0)
positives = sum(1 for i in list if i > 0)
zeros = sum(1 for i in list if i == 0)

print("Случайный список:", list)
print(f"Минимальный элемент: {min}")
print(f"Максимальный элемент: {max}")
print(f"Количество отрицательных элементов: {negatives}")
print(f"Количество положительных элементов: {positives}")
print(f"Количество нулей: {zeros}")