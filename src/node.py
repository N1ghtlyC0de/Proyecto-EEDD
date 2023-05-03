#Se define la clase nodo que recibe los parametros de "data" que seria el precio y "serial" que vendria siendo el serial del producto

class Node():
  def __init__(self, serial=None, data=None):
    self.data = data
    self.serial = serial
    self.prev = None
    # self.tail = None
    self.next = None