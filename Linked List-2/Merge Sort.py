class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge(head1,head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    ftail=None
    fhead=None
    
    #print(head1.data,head2.data)
    while head1 is not None and head2 is not None:
        if head1.data<=head2.data:
            if fhead is not None:
                ftail.next=head1
                ftail=ftail.next
            else:
                fhead=head1
                ftail=head1
            
            head1=head1.next
        else:
            if fhead is not None:
                ftail.next=head2
                ftail=ftail.next
            else:
                fhead=head2
                ftail=head2

            head2=head2.next
    while head1 is not None:
        ftail.next=head1
        ftail=ftail.next
        head1=head1.next
    while head2 is not None:
        ftail.next=head2
        ftail=ftail.next
        head2=head2.next
    ftail.next=None
    return fhead


def mergeSort(head):
    
    if head.next is None or head is None:
        return head
    fast=head
    slow=head
    while fast.next is not None and fast.next.next is not None:
        slow=slow.next
        fast=fast.next.next
    
    mid=slow
    h1=head
    h2=mid.next
    
    mid.next=None
    left=mergeSort(h1)
    right=mergeSort(h2)
    shead=merge(left,right)
    return shead
    

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
l = mergeSort(l)
#printll(l)
printll(l)