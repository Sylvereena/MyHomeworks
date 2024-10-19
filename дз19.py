grades = []
print("Введите 10 оценок студента от 1 до 12:")
for i in range(10):
    while True:
        try:
            grade = int(input(f"Оценка {i + 1}: "))
            if 1 <= grade <= 12:
                grades.append(grade)
                break
            else:
                print("Оценка должна быть от 1 до 12.")
        except ValueError:
                print("Введите число.")

while True:
    print("1. Оценки")
    print("2. Пересдача экзамена")
    print("3. Стипендия")
    print("4. Отсортированный список")
    print("5. Выход")

    choice = input("Выберите 1-5: ")

    match choice:
        case '1':
            print("Оценки:", grades)

        case '2':
            while True:
                try:
                    index = int(input("Введите номер 1-10: "))
                    if 1 <= index <= len(grades):
                        new_grade = int(input("Введите новую оценку (от 1 до 12): "))
                        if 1 <= new_grade <= 12:
                            grades[index] = new_grade
                            print(f"Оценка {index + 1} обновлена на {new_grade}.")
                            break
                        else:
                            print("Оценка должна быть от 1 до 12.")
                    else:
                        print("Номер вне диапазона.")
                except ValueError:
                    print("Введите число.")

        case '3':
            average = sum(grades) / len(grades)
            if average >= 10.7:
                print(f"Стипендия выходит")
            else:
                print(f"Стипендия не выходит")

        case '4':
            while True:
                try:
                    order = int(input("Выводить по возрастанию или убыванию? (1/2): "))
                    if order == 1:
                        sorted_grades = sorted(grades)
                        break
                    elif order == 2:
                        sorted_grades = sorted(grades, reverse=True)
                        break
                    else:
                        print("Выберите '1' для возрастания или '2' для убывания.")
                except ValueError:
                    print("Выберите '1' для возрастания или '2' для убывания.")

            print("Отсортированные оценки:", sorted_grades)

        case '5':
            break

        case _:
            print("Выберите от 1 до 5.")