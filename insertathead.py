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
def insertNodeAtHeadOfTail(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    newBlock.next = head
    return newBlock
l = [11,22,34,55,66,788,77]
head = None
for ele in l:
    head = insertNodeAtHeadOfTail(head, ele)
printLinkedList(head)
