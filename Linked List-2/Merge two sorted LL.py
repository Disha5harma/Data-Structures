#Merge two sorted LL

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge(head1,head2):
   
    ftail=None
    fhead=None
    while head1 is not None and head2 is not None:
        if head1.data<head2.data:
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
arr1=list(int(i) for i in input().strip().split(' '))
arr2=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l1 = ll(arr1[:-1])
l2 = ll(arr2[:-1])
l = merge(l1, l2)
printll(l)
