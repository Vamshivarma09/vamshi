class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class root:
    def __init__(self,):
        self.head = None


    def display(self):
        while self.head is not  None:
            print(self.head.item)
            self.head = self.head.next

    def insertatend(self,newdata):
        newnode = Node(newdata)
        if self.head == None:
            self.head = newnode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = newnode        
        

lst = root()
lst.head = Node("rebal")
second = Node("chirutha")
third = Node("businessman")
fourth = Node("bahubali")



lst.head.next = second
second.next = third
third.next = fourth

lst.insertatend("rrr")
lst.display()