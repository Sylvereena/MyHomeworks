from colorama import init, Fore, Back, Style
init() 


def color(color):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(color, end='')
            result = func(*args, **kwargs)
            print(Style.RESET_ALL, end='') 
            return result
        return wrapper
    return decorator

@color(Fore.BLUE)
def my_function():
    print("Каждый охотник желает знать, где сидит фазан")


my_function()