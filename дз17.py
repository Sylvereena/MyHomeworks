import warnings

def check(*arg_types, **kwarg_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, expected_type in zip(args, arg_types):
                if not isinstance(arg, expected_type):
                    warnings.warn(f"Аргумент {arg} к '{func.__name__}' должен быть {expected_type.__name__}, "
                                  f"вместо этого {type(arg).__name__}.", UserWarning)

            for key, expected_type in kwarg_types.items():
                if key in kwargs and not isinstance(kwargs[key], expected_type):
                    warnings.warn(f"Аргумент '{key}' to '{func.__name__}' должен быть {expected_type.__name__}, "
                                  f"вместо этого {type(kwargs[key]).__name__}.", UserWarning)

            return func(*args, **kwargs)
        return wrapper
    return decorator

@check(int, str, kwarg1=float)
def my_function(a, b, kwarg1=0.0):
    print(f"a: {a}, b: {b}, kwarg1: {kwarg1}")

my_function(10, "a", kwarg1=1.2)

my_function("10", 2, kwarg1="1.2")  # Предупреждение о типах