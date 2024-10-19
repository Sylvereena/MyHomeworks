def logger(func):
    """
    Декоратор, который ведет журнал вызовов декорируемой функции.
    Записывает имя функции, переданные аргументы и значения по умолчанию. 
    В случае возникновения исключения, логирует его имя и сообщение.
    :func: Декорируемая функция.
    :return: Функция-обертка.
    """

    def wrapper(*args, **kwargs):
        """
        Функция-обертка для записи информации о вызовах декорируемой функции.
        Логирует имя функции, ее аргументы, значения по умолчанию, результат выполнения функции или информацию об исключении.
        :args: Позиционные аргументы.
        :kwargs: Ключевые аргументы.
        :return: Результат выполнения декорируемой функции или None.
        """
        # имя функции
        func_name = func.__name__
        
        # значения по умолчанию
        defaults = func.__defaults__ or ()
        kw_defaults = func.__kwdefaults__ or {}
        
        # строка с аргументами
        args_list = [repr(arg) for arg in args]
        kwargs_list = [f"{key}={repr(value)}" for key, value in kwargs.items()]
        
        # значения по умолчанию к аргументам
        all_args = args_list + [
            f"{key}={repr(defaults[i])}" for i, key in enumerate(kw_defaults.keys()) if i < len(defaults)
        ]
        
        # строка журнала
        args_string = ', '.join(all_args)
        log_message = f"{func_name}({args_string})"
        
        try:
            result = func(*args, **kwargs)
            print(f"{log_message} -> {result}")
            return result
        except Exception as e:
            # исключение
            print(f"{log_message} .. {type(e).__name__}: {str(e)}")
            return None

    return wrapper

@logger

def plur_round(num1, num2, *, digits=0):
    return round(num1 * num2, digits)

# Пример тестирования
# >>> plur_round(2.5, 1.3, digits=2)
# >>> plur_round(5.1, 3.2)
# >>> plur_round(5.1, 'a')
# plur_round(2.5, 1.3) -> 3.25
# plur_round(5.1, 3.2) -> 16.0
# plur_round(5.1, 'a') .. TypeError: can't multiply sequence by non-int of type 'float'