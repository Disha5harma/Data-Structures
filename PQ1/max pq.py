# Code : Max Priority Queue
# Send Feedback
# Implement the class for Max Priority Queue which includes following functions -
# 1. getSize -
# Return the size of priority queue i.e. number of elements present in the priority queue.
# 2. isEmpty -
# Check if priority queue is empty or not. Return true or false accordingly.
# 3. insert -
# Given an element, insert that element in the priority queue at the correct position.
# 4. getMax -
# Return the maximum element present in the priority queue without deleting. Return -Infinity if priority queue is empty.
# 5. removeMax -
# Delete and return the maximum element present in the priority queue. Return -Infinity if priority queue is empty.
# Note : main function is given for your reference which we are using internally to test the class.


class priorityQueueNode:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority
class PriorityQueue:
    def __init__(self):
        self.pq=[]
        
    def isEmpty(self):
        return self.getSize()==0
        pass
    
    def getSize(self):
        return len(self.pq)
        pass

    def getMax(self):
        if self.getSize()==0:
            return None
        return self.pq[0].value
        pass
    def __percolateup(self):
        childindex=self.getSize()-1
        while childindex>0:
            parentindex=(childindex-1)//2
            if self.pq[childindex].priority>self.pq[parentindex].priority:
                self.pq[childindex],self.pq[parentindex]=self.pq[parentindex],self.pq[childindex]
                childindex=parentindex
            else:
                break
    def insert(self,ele,priority):
        pqnode=priorityQueueNode(ele,priority)
        self.pq.append(pqnode)
        self.__percolateup()
        pass
        
    def removeMax(self):
        #Implment This Function Here
        if self.isEmpty()==True:
            return None
        ele=self.pq[0].value
        self.pq[0]=self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolatedown()
        return ele
        pass
    
    def __percolatedown(self):
        parentindex=0
        leftchildindex=2*parentindex+1
        rightchildindex=2*parentindex+2
        
        while leftchildindex<self.getSize():
            minindex=parentindex
            if self.pq[minindex].priority<self.pq[leftchildindex].priority:
                
                minindex=leftchildindex
            if rightchildindex<self.getSize() and self.pq[minindex].priority<self.pq[rightchildindex].priority:
                
                minindex=rightchildindex
            if minindex==parentindex:
                break
            self.pq[minindex],self.pq[parentindex]=self.pq[parentindex],self.pq[minindex]
            parentindex=minindex
            leftchildindex=2*parentindex+1
            rightchildindex=2*parentindex+2
        
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1
