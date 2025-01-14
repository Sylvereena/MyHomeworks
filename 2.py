def deck():
    """
    Генераторная функция, создающая упорядоченную колоду карт.
    Возвращает кортеж из двух элементов: (номинал, масть).
    Номиналы: 2-10, 11-валет, 12-дама, 13-король, 14-туз.
    Масти: 'черви', 'бубны', 'пики', 'трефы'.
    """
    suits = ['черви', 'бубны', 'пики', 'трефы']
    for suit in suits:
        for rank in range(2, 15):  # 2-14, где 11 - валет, 12 - дама, 13 - король, 14 - туз
            yield (rank, suit)

# Пример тестирования
# >>> list(deck())[::8]
# [(2, 'черви'), (10, 'черви'), (5, 'бубны'), (13, 'бубны'), (8, 'пики'), (3, 'трефы'), (11, 'трефы')]