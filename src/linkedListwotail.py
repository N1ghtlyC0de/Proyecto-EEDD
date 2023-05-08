from node import Node
class LinkedListwotail():
    def __init__(self):
        self.head = None

    def append(self, serial, data):
        new_node = Node(serial, data)
        if self.head==None:
            self.head=new_node          
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node
    
    def clear(self):
        self.head=None


    

    