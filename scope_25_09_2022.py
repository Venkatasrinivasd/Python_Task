'''y = 10


def inner():
    x = 4
    print("x : ", x)
    print("inside the function y: ", y)


print("outside function y: ", y)
inner()'''
'''y = 10


def inner():
    x = 4
    global y
    y = y + 1
    print("x : ", x)
    print("inside the function y: ", y)


print("outside function y: ", y)
inner()'''
y = 10


def outer():
    z = 4

    def spinner():
        x = 4
        nonlocal z
        z = z + 1
        print("x : ", x)
        print("inside the function z: ", z)
    spinner()
    print("z :", z)


outer()

x = 5



def fun1():
    x = 10

    def inner():
        x = 15
        print("x: ", x)

    inner()


fun1()


