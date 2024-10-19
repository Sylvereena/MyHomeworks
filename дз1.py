while True:
        try:
            n1 = float(input("Введите первое число: "))
            n2 = float(input("Введите второе число: "))
            n3 = float(input("Введите третье число: "))
            break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

choose = input("Введите 'сумма' для сложения или 'произведение' для умножения: ").strip().lower()


while True:
        choose = input("Введите 'сумма' для сложения или 'произведение' для умножения: ").strip().lower()
        
        if choose == 'сумма':
            res = n1 + n2 + n3
            print(f"Сумма чисел: {res}")
            break
        elif choose == 'произведение':
            res = n1 * n2 * n3
            print(f"Произведение чисел: {res}")
            break
        else:
            print("Некорректный ввод. Пожалуйста, попробуйте еще раз.")