class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

class Root:
    def __init__(self):
        self.head=None

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.item) 
            temp = temp.next

    def insertatstart(self,newitem):
        newnode = Node(newitem) 
        newnode.next =  self.head
        self.head = newnode      

                
        
lst=Root()
lst.head = Node("nihar")
second = Node("srinavas")
third = Node("sakalesh")
fourth = Node("vasmhi")


lst.head.next = fourth
fourth.next = third
third.next = second


lst.insertatstart("kumar")


lst.display()