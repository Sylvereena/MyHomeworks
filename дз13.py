def get_discount(age):
    match age:
        case age if age < 3:
            return 10
        case age if 3 <= age < 6:
            return 20
        case age if 6 <= age < 10:
            return 30
        case age if 10 <= age < 14:
            return 40
        case age if age >= 14:
            return 50
        case _:
            return 0

ages = []
while True:
        age_input = input("Введите возраст ребенка или нажмите ввод для завершения: ")
        
        if age_input == '':
            break
        
        try:
            age = int(age_input)
            if age < 0:
                print("Возраст не может быть отрицательным. Попробуйте снова.")
                continue
            elif age > 18:
                print("Не ребенок. Попробуйте снова.")
                continue

            ages.append(age)
            discount = get_discount(age)
            print(f"Возраст: {age} лет, Скидка: {discount}%")
        except ValueError:
            print("Пожалуйста, введите корректное число или нажмите ввод для завершения.")

print("\nСписок:")
for age in ages:
        discount = get_discount(age)
        print(f"Возраст: {age} лет, Скидка: {discount}%")