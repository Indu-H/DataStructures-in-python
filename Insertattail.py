class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end = "-->")
        curr = curr.next
    print()

def insertAtEndOfTail(head,ele):
    newblock = Node(ele)
    if head == None:
        return newblock
    
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = newblock
    return head
l = [11,22,34,55,66,788,77]
head = None
for ele in l:
    head = insertAtEndOfTail(head, ele)
printLinkedList(head)


