stack = []
stack.append(30)
stack.append(20)
stack.append(10)
print(stack)
stack.pop()
print(stack)

stack2 = []


def push():
    element = input("enter a element into stack: ")
    stack2.append(element)
    print(stack2)


def pop():
    if not stack2:
        print("stack is empty : ")
    else:
        e = stack2.pop()
        print("removed element is : ", e)
        print(stack2)


while True:
    print(" select the operation 1. push 2. pop 3. quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("enter the correct option!")
