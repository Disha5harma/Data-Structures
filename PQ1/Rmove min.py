# Code : Remove Min
# Send Feedback
# Implement the function RemoveMin for the min priority queue class.
# For a minimum priority queue, write the function for removing the minimum element present. Remove and return the minimum element.
# Note : main function is given for your reference which we are using internally to test the code.


class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
            
    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
        
    def removeMin(self):
        #Implment This Function Here
        if self.isEmpty()==True:
            return None
        ele=self.pq[0].ele
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
            if self.pq[minindex].priority>self.pq[leftchildindex].priority:
                
                minindex=leftchildindex
            if rightchildindex<self.getSize() and self.pq[minindex].priority>self.pq[rightchildindex].priority:
                
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
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
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