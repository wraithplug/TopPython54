is_admin = True


def check_if_admin(func):
    def wrapper():
        if is_admin == True:
            func()
        else:
            print("Доступ запрещен")
    return wrapper

@check_if_admin
def say_hi():
    print("Hello world")

say_hi()
