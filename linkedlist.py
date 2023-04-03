class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Link:
    def __init__(self):
        self.head = None

lnk = Link()
lnk.head=Node("vasmhi")
second = Node("sakelesh")
third = Node("srinivas")
fourth = Node("sameer")

lnk.head.next=second
second.next=third
third.next=fourth

while lnk.head!=None:
    print(lnk.head.data)
    lnk.head=lnk.head.next