def math_function_resolver(func, *args, res_to_str=False):
    """
    Вычисляет округленные значения для заданной математической функции.

    :func: Математическая функция, принимающая одно число (x).
    :args: Произвольное количество значений x для вычисления.
    :res_to_str: Если True, возвращает результаты в виде строк; если False, в виде целых чисел.
    :return: Список округленных значений, либо int, либо str, в зависимости от значения res_to_str.
    """
    # Применяем функцию и округляем результаты в одной итерации
    results = [round(func(x)) for x in args]
    
    # Преобразуем результаты в строки, если необходимо
    if res_to_str:
        results = list(map(str, results))

    return results

# Примеры тестирования
# >>> math_function_resolver(lambda x: 1.5 * x + 2, *range(1, 10)) 
# [4, 5, 6, 8, 10, 11, 12, 14, 16]
# >>> math_function_resolver(lambda x: -2 * x - 2, *range(1, 10)) 
# [-4, -6, -8, -10, -12, -14, -16, -18, -20]
# >>> math_function_resolver(lambda x: 1.34 ** x, *range(1, 10), res_to_str=True)
# ['1', '2', '2', '3', '4', '6', '8', '10', '14']