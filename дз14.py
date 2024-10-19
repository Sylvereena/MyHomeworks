def get_category(score):
    match score:
        case score if score < 50:
            return "Новичок"
        case score if 50 <= score < 100:
            return "Любитель"
        case score if 100 <= score < 150:
            return "Опытный"
        case score if 150 <= score < 200:
            return "Профессионал"
        case _:
            return "Мастер"

players = []

while True:
        name = input("Введите имя игрока или нажмите ввод для завершения: ")
        if name == '':
            break

        scores = []
        for i in range(1, 6):
            while True:
                try:
                    score = int(input(f"Введите очки за бросок {i} (0-100): "))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("Очки должны быть в диапазоне от 0 до 100.")
                except ValueError:
                    print("Пожалуйста, введите корректное число.")

        total = sum(scores)
        category = get_category(total)

        players.append((name, total, category))


print("\nРезультаты турнира:")
for player in players:
    print(f"Игрок: {player[0]}, Очки: {player[1]}, Категория: {player[2]}")