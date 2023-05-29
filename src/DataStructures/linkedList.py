from DataStructures.node import Node

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
    self.tail = None
      
  def print_list(self):
    current = self.head
    while current is not None:
      print(current.data)
      current = current.next
          
  def delete(self, data):
    if self.head is None:
      return
    if self.head.data == data:
      self.head = self.head.next
      if self.head:
        self.head.prev = None
      else:
        self.tail = None
      return
    current_node = self.head
    while current_node.next:
      if current_node.next.data == data:
        current_node.next = current_node.next.next
        if current_node.next:
          current_node.next.prev = current_node
        else:
          self.tail = current_node
        return
      current_node = current_node.next
    self.head = None