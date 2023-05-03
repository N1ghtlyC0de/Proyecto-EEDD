from node import Node

class DoubleLinkedList():
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, serial, data):
    new_node = Node(serial, data)
    if self.head is None:
        self.head = new_node
    else:
        self.tail.next = new_node
        new_node.prev = self.tail
    self.tail = new_node

  def clear(self):
    self.head = None
    self.tail = None  