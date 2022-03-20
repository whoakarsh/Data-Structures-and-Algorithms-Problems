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

    def reverse(self,head):
        if head is None or head.next is None:
            return head
        rest = self.reverse(head.next)
        head.next.next = head 
        head.next = None
        return rest

l = LinkedList()
nodes_val = [1,2,3,4,5]
for val in nodes_val:
    l.insertAtEnd(val)
l.print() #=>1 2 3 4 5 
l.head = l.reverse(l.head)
l.print() #=> 5 4 3 2 1