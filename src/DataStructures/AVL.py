class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.height = 0

class AVLTree:
  def __init__(self):
    self.root = None

  def insertAVL(self, data):
    self.root = self.insert(data, self.root)

  def insert(self, data, node):
    if node is None:
      node = Node(data)  
    elif self.compareTo(data, node.data) < 0:
      node.left = self.insert(data, node.left) 
    elif self.compareTo(data, node.data) > 0:
      node.right = self.insert(data, node.right)
      
    node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
    node = self.rebalance(node)
    return node

  def common(self, node1, node2):
    current = self.root
    while current is not None:
      if self.compareTo(node1.data, current.data) < 0 and self.compareTo(node2.data, current.data) < 0:
        current = current.left
      elif self.compareTo(node1.data, current.data) > 0 and self.compareTo(node2.data, current.data) > 0:
        current = current.right
      else:
        break
    return current

  def findNode(self, data, node):
    if node is None or self.compareTo(data, node.data) == 0:
      return node
    elif self.compareTo(data, node.data) < 0:
      return self.findNode(data, node.left)
    else:
      return self.findNode(data, node.right)
          
  def balanceFactor(self, node):
    if node is None:
      return 0
    return self.getHeight(node.right) - self.getHeight(node.left)

  def rotateLeft(self, node):
    rightChild = node.right
    node.right = rightChild.left
    rightChild.left = node
    node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
    rightChild.height = 1 + max(self.getHeight(rightChild.left), self.getHeight(rightChild.right))
    return rightChild

  def rotateRight(self, node):
    leftChild = node.left
    node.left = leftChild.right
    leftChild.right = node
    node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
    leftChild.height = 1 + max(self.getHeight(leftChild.left), self.getHeight(leftChild.right))
    return leftChild

  def rebalance(self, node):
    balanceFactor = self.balanceFactor(node)
    if balanceFactor < -1:
      if self.balanceFactor(node.left) <= 0:
        node = self.rotateRight(node)
      else:
        node.left = self.rotateLeft(node.left)
        node = self.rotateRight(node)
    if balanceFactor > 1:
      if self.balanceFactor(node.right) >= 0:
        node = self.rotateLeft(node)
      else:
        node.right = self.rotateRight(node.right)
        node = self.rotateLeft(node)
    return node

  def compareTo(self, node1, node2):
    if isinstance(node1, str) and isinstance(node2, str):
      string1 = node1
      string2 = node2
      lenStr1 = len(string1)
      lenStr2 = len(string2)
      minStr = min(lenStr1, lenStr2)

      for i in range(minStr):
        char1 = string1[i]
        char2 = string2[i]
        if char1 != char2:
          return ord(char1) - ord(char2)
      return lenStr1 - lenStr2
      
  def getHeight(self, node):
    if node is None:
      return 0
    return node.height
      
  def getDistance(self, startNode, endNode):
    startToRoot = self.getPathLength(startNode)
    endToRoot = self.getPathLength(endNode)
    commonAncestor = self.getPathLength(self.common(startNode, endNode))
    distance = startToRoot + endToRoot - 2 * commonAncestor + 1
    return distance
    
  def getMinDistance(self, start, end):
    startNode = self.findNode(start, self.root)
    endNode = self.findNode(end, self.root)
    distance = self.getDistance(startNode, endNode)
    return distance

  def getPathLength(self, node):
    length = 0
    current = self.root
    while current is not None:
      if self.compareTo(node.data, current.data) < 0:
        current = current.left
      elif self.compareTo(node.data, current.data) > 0:
        current = current.right
      else:
        break
      length += 1
    return length