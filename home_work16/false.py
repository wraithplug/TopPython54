def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Начало")
        result = func(*args, **kwargs)
        print(result)
        print("Конец")
        return result
    return wrapper
@my_decorator
def add(a,b):
    return a+b

add(1,2)
