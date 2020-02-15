# def florr(arr,x):
# 	if arr[0]>=x:
# 		return arr[0]
# 	arr=arr[1:]
# 	return florr(arr,x)

# x=int(input())
# arr=list(int(i) for i in input().strip().split(" "))
# print(florr(arr,x))
# arr=list(int(i) for i in input().strip().split(" "))
# n=arr[0]
# m=arr[1]
# if m%n==0:
#     ans=(m//n)-1
#     ans=ans*n
# else:
#     ans1=((m//n)-1)*n
#     ans2=(m%n)*n
#     ans=ans1+ans2
# print(ans)
# 
# arr=list(int(i) for i in input().strip().split(" "))
# n=arr[0]
# m=arr[1]
# def mgreater(m,n):
#     if m%n==0:
#         ans=((m//n)-1)*n
#     else:
#         ans1=((m//n)-1)*n
#         ans2=(m%n)*n
#         ans=ans1+ans2
#     return ans
# if m>n:
#     fans=mgreater(m,n)
# else:
#     if n%m==0:
#         fans=0
#     else:
#         ans1=mgreater(m,(n%m))
#         ans2=n//m
#         fans=ans1+ans2
       
# print(fans)
# # def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n*fact(n-1)
# arr1=list(int(i) for i in input().strip().split(" "))
# arr2=list(int(i) for i in input().strip().split(" "))
# print(fact(arr1[1]))
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

def nth(head,n):
	if head==None:
		return null
	p1=head
	p2=head
	for j in range(n):
		if p2==None:
			return None
		p2=p2.next
	while p2.next is not None:
		p1=p1.next
		p2=p2.next
		#print('*'+str(p1.data))
	return p1


arr=list(int(i) for i in input().strip().split(" "))
l=makell(arr)
i=int(input())
node=nth(l,i)
if node:
	print(node.data)