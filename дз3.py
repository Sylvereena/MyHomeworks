while True:
        try:
            ms = float(input("Введите количество метров: "))
            break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

while True:
        choose = input("Введите 'мили', 'дюймы' или 'ярды'").strip().lower()
        
        if choose == 'мили':
            res = ms * 0.000621371
            print(f"{ms} метров = {res} миль")
            break
        elif choose == 'дюймы':
            res = ms * 39.3701
            print(f"{ms} метров = {res} дюймов")
            break
        elif choose == 'ярды':
            res = ms * 1.09361
            print(f"{ms} метров = {res} ярдов")
            break
        else:
            print("Некорректный ввод.")