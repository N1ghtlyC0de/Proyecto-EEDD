from node import Node
class Stack():
  def __init__(self):
    self.top = None
    self.bottom = None
    self.size = 0

  def push(self, n,m):
    newNode = Node(n, m)
    if self.top is None:
        self.top = newNode
    else:
        self.bottom.next = newNode
        newNode.prev = self.bottom
    self.bottom = newNode

  def pop(self):
    n = self.top.next
    self.top.next = None
    a = self.top.data
    self.top = n
    n = None
    return a

  def __len__(self):
    return self.size