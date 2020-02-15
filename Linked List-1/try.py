arr=list(int(i) for i in input().strip().split(' '))
arr1=[0]*arr[0]
def check(arr):
    c=0
    for ele in arr:
        if ele==1:
            c+=1
    return c
for j in range(arr[1]):
    choice=input()
    if choice=='CLICK 1':
        if arr1[0]==0:
            arr1[0]=1
        else:
            arr1[0]=0
        
    elif choice=='CLICK 2':
        if arr1[1]==0:
            arr1[1]=1
        else:
            arr1[1]=0
    elif choice=='CLICK 3':
        if arr1[2]==0:
            arr1[2]=1
        else:
            arr1[2]=0
    else:
        arr1=[0]*arr[0]
    print(check(arr1))
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# def len(head):
#     count=0
#     while head.next!=None:
#         count+=1
#         head=head.next
    
#     return count

# def delmid(head):
#     mid=len(head)//2
#     curr=head
#     for i in range(mid):
#     	curr=curr.next
#     temp=curr
#     temp.next=curr.next
#     return head

# def makell(arr):
#     if len(arr)==0:
#         return None
#     head=node(arr[0])
#     last=head
#     for ele in arr[1:]:
#         last.next=node(ele)
#         last=last.next
#     return head

# def printll(head):
	
#     while head.next is not None:
#         print(head.data,'->',end="")
#         head=head.next
#     print(head.data)    
    
# arr=list(int(i) for i in input().strip().split(' '))
# head=makell(arr)
# delmid(head)
# printll(head)
