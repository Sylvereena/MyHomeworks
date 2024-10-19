while True:
        try:
            n1 = float(input("Введите первое число: "))
            n2 = float(input("Введите второе число: "))
            n3 = float(input("Введите третье число: "))
            break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

while True:
        choose = input("Введите 'максимум', 'минимум' или 'среднее': ").strip().lower()
        
        if choose == 'максимум':
            res = max(n1, n2, n3)
            print(f"Максимум из чисел: {res}")
            break
        elif choose == 'минимум':
            res = min(n1, n2, n3)
            print(f"Минимум из чисел: {res}")
            break
        elif choose == 'среднее':
            res = (n1 + n2 + n3) / 3
            print(f"Среднеарифметическое чисел: {res}")
            break
        else:
            print("Некорректный ввод.")