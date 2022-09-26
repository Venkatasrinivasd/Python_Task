def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner


@str_upper
def print_str():
    return "good morning"


print(print_str())


def di_decorator(func):
    def inner(x, y):
        if y == 0:
            return "give a proper input"
        return func(x, y)
    return inner


@di_decorator
def div(a, b):
    return a / b


print(div(4, 5))


def outer(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner()


@outer
def print_str():
    return "good mornig"


print(print_str)