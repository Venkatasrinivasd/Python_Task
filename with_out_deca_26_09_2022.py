def function1():
    print("hi i am function1")


def function2(func):
    print("hi i am function 2 now i will cal functional")
    func()


function2(function1)


def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner


def print_str():
    return "good morning"


print(print_str())
d = str_upper(print_str)
print(d())
