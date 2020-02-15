class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

def take_input():
	l=[int(i) for i in input().split()]
	head=None
	tail=None
	for currd in l:
		if currd == -1:
			return head
		newnode=Node(currd)
		if head is None:
			head=newnode
			tail=newnode
		else:
			tail.next=newnode
			tail=newnode
	return head

def printl(head):
	while head is not None:
		print(head.data,end=" ")
		head=head.next

def length(head):
	c=0
	while head is not None:
		c+=1
		head=head.next

def insertlR(head,i,x):
	if i<0:
		return head

	if i==0:
		newnode=Node(x)
		newnode.next=head
		return newnode
	smallhead=insertlR(head.next,i-1,x)
	head.next=smallhead


	if head is None:
		return None
	
	return head

head=take_input()
printl(head)
print("\r")
insertlR(head,3,9)
printl(head)