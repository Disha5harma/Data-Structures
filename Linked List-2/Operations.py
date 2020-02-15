# Find a node in LL (recursive)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linearSearchRecursive(head, n):
    
    curr=head
    c=0
    while curr is not None:
        if curr.data==n:
            return c
        curr=curr.next
        c+=1
    return -1
    pass

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
data=int(input())
index = linearSearchRecursive(l, data)
print(index)


# Even after Odd LinkedList
# Sample Input 1 :
# 1 4 5 2 -1
# Sample Output 1 :
# 1 5 4 2 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrange_LinkedList(head):
   
    ohead=None
    ehead=None
    otail=None
    etail=None
    curr=head
    while curr is not None:
        if curr.data%2==0:
            if ehead is None:
                ehead=curr
                etail=curr
            else:
                etail.next=curr
                etail=curr
        else:
            if ohead is None:
                head=curr
                ohead=curr
                otail=curr
            else:
                otail.next=curr
                otail=curr
        curr=curr.next
    if otail is None:
        head=ehead
    elif etail is not None :
        otail.next=ehead
        etail.next=None
    return head        
 
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
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = arrange_LinkedList(l)
printll(l)