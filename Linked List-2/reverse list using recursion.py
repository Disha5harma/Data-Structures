class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findtail(head):
    if head is not None:
        head=head.next
        tail=head
    return tail
def reverseRecursive(head):
   
    if head.next is None or head is None:
        return head
    h=reverseRecursive(head.next)
    tail=findtail(head)
    tail.next=head
    head.next=None
    
    return h
    

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = reverseRecursive(l)
printll(l)