
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def length(head):
    c=0
    while head is not None:
        c+=1
        head=head.next
    return c

def delete(head, i):
    if i<0 or i>length(head)-1:
        return head
    prev=None
    curr=head
    c=0
    while c<i:
        prev=curr
        curr=curr.next
        c+=1
    curr=curr.next
    if prev is not None:
        prev.next=curr
    else:
        head=curr
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