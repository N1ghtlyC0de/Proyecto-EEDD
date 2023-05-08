from node import Node
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, serial,data):
        new_node = Node(serial, data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def clear(self):
        self.head = None