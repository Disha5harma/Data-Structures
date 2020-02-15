class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

def ll(arr):
	if len(arr)==0:
		return None
	head=Node(arr[0])
	last=head
	for data in arr[1:]:
		last.next=Node(data)
		last=last.next
	return head

def linearsearchrecur(head,n):
	if(head==None):
		return -1
	if(head.data==n):
		return 0
	result=linearsearchrecur(head.next,n)
	if(result==-1):
		return -1
	return 1+result

arr=list(int(i) for i in input().strip().split(" "))
l=ll(arr[:-1])
data=int(input())
index=linearsearchrecur(l,data)
print(index)
