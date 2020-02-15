# kReverse
# Send Feedback
# Implement kReverse( int k ) in a linked list i.e. you need to reverse first K elements then reverse next k elements and join the linked list and so on.
# Indexing starts from 0. If less than k elements left in the last, you need to reverse them as well. If k is greater than length of LL, reverse the complete LL.
# You don't need to print the elements, just return the head of updated LL.
# Input format :

# Line 1 : Linked list elements (separated by space and terminated by -1)

# Line 2 : k

# Sample Input 1 :
# 1 2 3 4 5 6 7 8 9 10 -1
# 4
# Sample Output 1 :
# 4 3 2 1 8 7 6 5 10 9
# Sample Input 2 :
# 1 2 3 4 5 -1
# 2
# Sample Output 2 :
# 2 1 4 3 5 
# Sample Input 3 :
# 1 2 3 4 5 6 7 -1
# 3
# Sample Output 3 :
# 3 2 1 6 5 4 7

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    count=0
    while head:
        count+=1
        head=head.next
    return count

def insertf(head,tail,x):
    newNode=Node(x)
    if not head:
        head=newNode
        tail=head
    else:
        newNode.next=head
        head=newNode
    return head,tail
def insert(pos,x):
    newNode=Node(x)
    newNode.next=pos.next
    pos.next=newNode
def kReverse(head, n) :
    #  Implement kReverse( k ) in a linked list i.e. you need to reverse
    #  first K elements then reverse next k elements and join the linked list and
    #  so on. Indexing starts from 0. If less than k elements left in the last,
    #  you need to reverse them as well. If k is greater than length of LL,
    #  reverse the complete LL. If n is 4 and LL is:
    #  Input: 1 2 3 4 5 6 7 8 9 10
    #  Output: 4 3 2 1 8 7 6 5 10 9 
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    l=length(head)
    k=n
    res=None
    tail=None
    for i in range(k):
        if i==l:
            break
        res,tail=insertf(res,tail,head.data)
        head=head.next
    while head:
        k=n
        while k:
            k-=1
            if not head:
                break
            insert(tail,head.data)
            head=head.next
        while tail.next:
            tail=tail.next
    return res
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
i=int(input())
l = kReverse(l, i)