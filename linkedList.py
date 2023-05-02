from node import Node

class LinkedList():
  def __init__(self):
    self.head = None
    self.length = 0

  def pushBack(self, data):
    curr = self.head
    newNode = Node(data)
    if self.head == None:
      self.head = newNode
    else:
      while curr.next != None:
        curr = curr.next
      curr.next = newNode
    self.length += 1
  
  def getHead(self):
    return self.head

  def getLength(self):
    return self.length