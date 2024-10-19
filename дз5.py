while True:
    number = input("Введите целое число: ")

    if number.isdigit():
        break
    else:
        print("Пожалуйста, введите число.")
    
res = ""

for num in number:
    if num in ('3', '6'):
        continue
    res += num
    if res == "": 
        res = "0"

print(f"Результат: {res}")
