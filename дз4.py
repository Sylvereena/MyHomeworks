while True:
    try:
        start = int(input("Введите первое число: "))
        end = int(input("Введите второе число: "))
        if start > end:
            start, end = end, start
        break
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")

even = 0
odd = 0 
nine = 0 
eCount = 0 
oCount = 0
nCount = 0

for num in range(start, end + 1):
    if num % 2 == 0:
        even += num
        eCount += 1
    else:
        odd += num
        oCount += 1
    
    if num % 9 == 0:
        nine += num
        nCount += 1
eAvg = even / eCount if eCount > 0 else 0
oAvg = odd / oCount if oCount > 0 else 0
nAvg = nine / nCount if nCount > 0 else 0

print(f"Сумма четных чисел: {even}, среднеарифметическое: {eAvg}")
print(f"Сумма нечетных чисел: {odd}, среднеарифметическое: {oAvg}")
print(f"Сумма чисел, кратных 9: {nine}, среднеарифметическое: {nAvg}")