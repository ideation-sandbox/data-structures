class Node():
    def __init__(self, val=None):
        self.val = val
        self.nextval = None

class LinkedList():
    def __init__(self):
        self.header = None #will contain a Node object

    def printcontent(self):
        value = self.header
        while value is not None:
            print(value.val)
            value = value.nextval


#testcode

node1 = Node('Mon')
node2 = Node('Tue')
node3 = Node('Wed')

linkedlist = LinkedList()
linkedlist.header = node1
node1.nextval=node2
node2.nextval=node3

linkedlist.printcontent()
