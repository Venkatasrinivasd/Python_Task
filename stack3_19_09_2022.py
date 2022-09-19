'''import collections
stack = collections.deque()
stack.append(10)
print(stack)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)'''


import queue
stack = queue.LifoQueue()
stack.put(10)
stack.put(30)
stack.put(40)

print(stack.get(40))
