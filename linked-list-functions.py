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

    def insert_beginning(self,val):
        item = self.header
        new_node = Node(val)
        self.header = new_node
        new_node.nextval = item

    def insert_end(self,val):
        new_node = Node(val)
        current_node = self.header
        if current_node is None:    #if header is empty
            self.header = new_node
            return
        while current_node.nextval: #iterate until last node is found
            current_node = current_node.nextval
        current_node.nextval = new_node

    def insert_data_bw(self, middle_node, newval):

        new_node = Node(newval)
        next_node = middle_node.nextval
        middle_node.nextval = new_node
        new_node.nextval = next_node



    def reverse(self):

        current = self.header
        prev = None

        while current!=None:

            self.header = current.nextval  # header updated to next node value in line
            current.nextval = prev # current node's next will be previous node
            prev = current # update previous for next iteration
            current = self.header # update current used in while loop iteration

        self.header = prev  # point head to latest accessible node



node1 = Node('Mon')
node2 = Node('Tue')
node3 = Node('Thur')

linkedlist = LinkedList()
linkedlist.header = node1
node1.nextval=node2
node2.nextval=node3
linkedlist.insert_beginning('Sun')
linkedlist.insert_end('Fri')
linkedlist.insert_data_bw(node2,'Wed')

linkedlist.printcontent()
linkedlist.reverse()
print('Reversed Linked List:')
linkedlist.printcontent()
