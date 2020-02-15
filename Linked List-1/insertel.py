class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
def inputl():
	l=[int(i) for i in input().split()]
	head=None
	tail=None
	for currd in l:
		if currd==-1:
			break
		newnode=Node(currd)
		if head is None:
			head=newnode
			tail=newnode
		else:
			tail.next=newnode
			tail=newnode
	return head

def length(head):
	c=0
	while head is not None:
		c+=1
		head=head.next
	return c

def insertl(head,i,x):
	if i<0 or i>length(head):
		return head
	
	c=0
	prev=None
	curr=head
	while i>c:
		prev=curr
		curr=curr.next
		c+=1
	newnode=Node(x)
	if prev is not None:
		prev.next=newnode
	else:
		head=newnode
	newnode.next=curr

	return head

def printl(head):
	while head is not None:
		print(head.data,"->",end="")
		head=head.next



head=inputl()
printl(head)
print('\r')
head1=insertl(head,0,10)
printl(head1)
print('\r')
printl(head)




