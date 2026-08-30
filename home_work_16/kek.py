from operator import add


def my_decorartor(func):
    def wrap(*args, **kwargs):
        return 2 * func(*args, **kwargs)

    return wrap
@my_decorartor
def add(a,b):
    return a+b
print(add(2,3))
