class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def makell(arr):
    if len(arr)==0:
        return None
    head=Node(arr[0])
    last=head
    for ele in arr[1:]:
        last.next=Node(ele)
        last=last.next
    return head

def length(head):
    c=0
    while head is not None:
        c+=1
        head=head.next
    return c

def ithNode(head, i):
    n=0
    curr=head
    while curr is not None:
        curr=curr.next
        n+=1
    if i>n:
        return
    else:
        for k in range(i):
            head=head.next
        return head

def printll(head):
    while head.next is not None:
        print(head.data,'->',end="")
        head=head.next
    print(head.data)

#ITERATIVELY
def insertati(head,i,data):
    if i<0 or i>length(head):
        return head
    count=0
    prev=None
    curr=head
    while count<i:
        prev=curr
        curr=curr.next
        count+=1
    newnode=Node(data)
    if prev is not None:
        prev.next=newnode
    else:
        head=newnode
    newnode.next=curr
    return head

#RECURSIVELY
def insertatiR(head,i,data):
    if i<0:
        return head
    if i==0:
        newnode=Node(data)
        newnode.next=head
        return newnode
    smallhead=insertatiR(head.next,i-1,data)
    head.next=smallhead
    return head
 
#ITERATIVE
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

#RECURSIVE
def deleteRec(head, i):
    if i<0 or i>length(head)-1:
        return head
    if i==0:
        head=head.next
        return head
    if head.data==-1:
        return None
        
    smallhead=deleteRec(head.next,i-1)
    head.next=smallhead
    return head   

#arr=list(int(i) for i in input().strip().split(" "))
arr=[int(ele) for ele in input().split()]
head=makell(arr)
print(length(head))
printll(head)
i=int(input("enter the position of node to be displayed"))
node = ithNode(head, i)
if node:
    print(node.data)
print("By Iteration")
pos=int(input("enter the position:"))
data=int(input("enter the data:"))
head=insertati(head,pos,data)
printll(head)
print("By Recursion")
pos=int(input("enter the position:"))
data=int(input("enter the data:"))
head=insertati(head,pos,data)
printll(head)
#Number of nodes in a linked list

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def length(head):
#     c=0
#     while head is not None:
#         c+=1
#         head=head.next
#     return c
#     pass

# def ll(arr):
#     if len(arr)==0:
#         return None
#     head = Node(arr[0])
#     last = head
#     for data in arr[1:]:
#         last.next = Node(data)
#         last = last.next
#     return head

# # Main
# # Read the link list elements including -1
# arr=list(int(i) for i in input().strip().split(' '))
# # Create a Linked list after removing -1 from list
# l = ll(arr[:-1])
# len=length(l)
# print(len)

#Print ith node
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def ithNode(head, i):
#     n=0
#     curr=head
#     while curr is not None:
#         curr=curr.next
#         n+=1
#     if i>n:
#         return
#     else:
#         for k in range(i):
#             head=head.next
#         return head
#     pass
# def length(head):
#     c=0
#     while head is not None:
#         c+=1
#         head=head.next
#     return c
#     pass
# def ll(arr):
#     if len(arr)==0:
#         return None
#     head = Node(arr[0])
#     last = head
#     for data in arr[1:]:
#         last.next = Node(data)
#         last = last.next
#     return head
# #ITERATIVELY
# def insertati(head,i,data):
#     if i<0 or i>length(head):
#         return head
#     count=0
#     prev=None
#     curr=head
#     while count<i:
#         prev=curr
#         curr=curr.next
#         count+=1
#     newnode=Node(data)
#     if prev is not None:
#         prev.next=newnode
#     else:
#         head=newnode
#     newnode.next=curr

#     return head

# #RECURSIVELY
# def insertatiR(head,i,data):
#     if i<0:
#         return head
#     if i==0:
#         newnode=Node(data)
#         newnode.next=head
#         return newnode
#     smallhead=insertatiR(head.next,i-1,data)
#     head.next=smallhead
#     return head


# # Main
# # Read the link list elements including -1
# arr=list(int(i) for i in input().strip().split(' '))
# # Create a Linked list after removing -1 from list
# l = ll(arr[:-1])
# i=int(input())
# node = ithNode(l, i)
# if node:
#     print(node.data)

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def take_input():
    
#     inputlist=[int(i) for i in input().split()]
#     head=None
#     for currd in inputlist:
#         if currd==-1:
#             break
#         newnode=Node(currd)
#         if head is None:
#             head=newnode
#         else:
#             curr=head
#             while curr.next is not None:
#                 curr=curr.next
#             curr.next=newnode
#     return head
# def print_list(head):
#     while head is not None:
#         print(head.data,"->",end="")
#         head=head.next
#     print("None")
    
# head=take_input()
# print_list(head)  


#OPTIMIZED METHOD

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# def inputl():
    
#     mylist=[int(i) for i in input().split()]
#     head=None
#     tail=None
#     for currd in mylist:
#         if currd==-1:
#             break
#         newnode=Node(currd)
#         if head is None:
#             head=newnode
#             tail=newnode
#         else:
#             tail.next=newnode
#             tail=newnode
#     return head

# def printl(head):
#     while head is not None:
#         print(head.data,"->",end="")
#         head=head.next
#     print("None")

# head=inputl()
# printl(head)

