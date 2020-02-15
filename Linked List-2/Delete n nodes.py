# Delete every N nodes

# Given a linked list and two integers M and N. Traverse the linked list such that you retain M nodes then delete next N nodes, continue the same until end of the linked list. That is, in the given linked list you need to delete N nodes after every M nodes.
# Input format :

# Line 1 : Linked list elements (separated by space and terminated by -1)

# Line 2 : M

# Line 3 : N

# Sample Input 1 :
# 1 2 3 4 5 6 7 8 -1
# 2
# 2
# Sample Output 1 :
# 1 2 5 6
# Sample Input 2 :
# 1 2 3 4 5 6 7 8 -1
# 2
# 3
# Sample Output 2 :
# 1 2 6 7

#See in pictures


Swap two Node of LL
Send Feedback
Given a linked list, i & j, swap the nodes that are present at i & j position in the LL. You need to swap the entire nodes, not just the data.
Indexing starts from 0. You don't need to print the elements, just swap and return the head of updated LL.
Assume i & j given will be within limits. And i can be greater than j also.
Input format :

Line 1 : Linked list elements (separated by space and terminated by -1)

Line 2 : i and j (separated by space)

Sample Input 1 :
3 4 5 2 6 1 9 -1
3 4
Sample Output 1 :
3 4 5 6 2 1 9
Sample Input 2 :
3 4 5 2 6 1 9 -1
2 4
Sample Output 2 :
3 4 6 2 5 1 9


#Your code


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
        
def swap_nodes(head, i, j):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    l=length(head)
    curr=head
    c1=curr
    p1=None
    for x in range(l):
        
        if x==i-1:
            p1=curr
            c1=curr.next
        if x==j-1:
            p2=curr
            c2=curr.next
        curr=curr.next
    
    p2.next=c1
    if i==0:
        head=c2
    if abs(j-i)==1:
        p2=c1
    elif abs(j-i)>2:
        p2=c1.next    

    if i!=0:
        p1.next=c2
        c1.next=c2.next
    c2.next=p2
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
i, j=list(int(i) for i in input().strip().split(' '))
l = swap_nodes(l, i, j)
printll(l)

