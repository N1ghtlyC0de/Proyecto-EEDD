from node import Node
class Stack():
  def __init__(self):
    self.top = None
    self.bottom = None
    self.size = 0

  def push(self, n,m):
    new_node = Node(n, m)
    if self.top is None:
        self.top = new_node
    else:
        self.bottom.next = new_node
        new_node.prev = self.bottom
    self.bottom = new_node

  def pop(self):
    n = self.top.next
    self.top.next = None
    a = self.top.data
    self.top = n
    n = None
    return a