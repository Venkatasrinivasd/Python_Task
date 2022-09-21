class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):   # it will display the data which are present in the linked list
        if self.head is None:   # if head contain none then linked list will be empty
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:  # node has any data linked list will be displayed
                print("--->", n.data, end=" ")
                n = n.ref

    def add_begin(self, data):   # add the node to linked list
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
                n.ref = new_node


ll1 = LinkedList()
ll1.add_begin(20)
ll1.add_end(5)
ll1.add_begin(10)
ll1.print_ll()

