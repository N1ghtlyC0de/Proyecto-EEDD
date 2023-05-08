from node import Node

class Queue():
  def __init__(self):
    self.front = None
    self.rear = None
    self.size = 0

  def enqueue(self, i, e):
    node = Node(i, e)
    if self.rear:
      self.rear.next = node
      self.rear = node
    else:
      self.rear = node
      self.front = node
    self.size += 1

  def dequeue(self):
    if not self.empty():
      currData = self.front.data
      curr = self.front
      self.front = self.front.next
      curr.next = None
      if not self.front:
        self.rear = None
      return currData
    else:
      raise Exception("Empty Queue.")
    self.size -= 1
      
  def clearQueue(self):
    self.front = None
    self.rear = None

  def __len__(self):
    return self.size
    
  def empty(self):
    return not self.front