from node import Node
class DoubleLinkedListwotail():
    def __init__(self):
        self.head = None
 
    def append(self, serial, data):
        new_node = Node(serial, data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def clear(self):
        self.head=None