# Code : Stack Using LL

# You need to implement a Stack class using linked list.
# The data members should be private.
# Implement the following public functions :
# 1. Constructor -
# Initialises the data member (i.e. head to null).
# 2. push :
# This function should take one argument of type T and has return type void. This function should insert an element in the stack. Time complexity should be O(1).
# 3. pop :
# This function takes no input arguments and has return type T. This should removes the last element which is entered and return that element as an answer. Time complexity should be O(1).
# 4. top :
# This function takes no input arguments and has return type T. This should return the last element which is entered and return that element as an answer. Time complexity should be O(1).
# 5. size :
# Return the size of stack i.e. count of elements which are present ins stack right now. Time complexity should be O(1).
# 6. isEmpty :
# Checks if the stack is empty or not. Return true or false.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class StackUsingLL:
    ### Implement all these functions here
    
    def __init__(self):
        self.__head = None
        self.__size = 0

    def push(self,data):
        newnode=Node(data)
        newnode.next=self.__head
        self.__head=newnode
        self.__size+=1
        return self.__head
        
    def pop(self):
        if self.__size ==0:
            return 0 
        x=self.__head
        self.__head=self.__head.next
        self.__size-=1
        return x.data
    # Return 0 if stack is empty. Don't display any other message
    def top(self):
        if self.__head is None:
            return 0
        return self.__head.data
    # Return 0 if stack is empty. Don't display any other message
    def isEmpty(self):
        return self.__size==0
    def getSize(self):
        return self.__size
    
s = StackUsingLL()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i+1])
        i+=1
    elif choice == 2:
        ans = s.pop()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        if(s.isEmpty()):
            print('true')
        else:
            print('false')
    i+=1
