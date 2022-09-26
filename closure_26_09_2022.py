def outer():
    x = 3

    def inner():
        print(x)
    inner()


outer()


def outer():
    x = 3

    def inner():
        print(x)
    return inner()


a = outer

print(a())


def outer():
    x = 3

    def inner():
        y = 3
        result = x + y
        return result
    return inner


a = outer()
print(a())


def outer():
    msg = "hello"

    def inner():
        print(msg)
    return inner


a = outer()
print(a())








