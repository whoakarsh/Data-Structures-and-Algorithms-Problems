class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        cur = self.head 
        while cur!=None:
            print(cur.val,end=" ")
            cur = cur.next
        print()

    def insertAtEnd(self,data):
        cur = self.head 
        newNode = Node(data)
        if cur==None:
            self.head = newNode
        else:
            while cur.next!=None:
                cur = cur.next 
            cur.next = newNode

    def deleteAtEnd(self):
        cur = self.head
        if cur==None or cur.next==None:
            self.head = None
        else:
            while cur.next.next!=None:
                cur = cur.next 
            cur.next = None

l = LinkedList()
nodes_val = [1,2,3,4,5]
for val in nodes_val:
    l.insertAtEnd(val)
l.print() # => 1 2 3 4 5 
l.deleteAtEnd()
l.print() # => 1 2 3 4
l.deleteAtEnd()
l.print()