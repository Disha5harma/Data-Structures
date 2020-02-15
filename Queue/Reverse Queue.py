# Reverse Queue

# Given a queue of integers, reverse it without help of any explicit stack or queue. You need to change in the given queue itself.
# Note : No need to return or print the queue.
# Input format :
# Line 1 : First Element - Size of Queue, Rest Elements - Elements Of Queue
# Output format :
# Queue elements
# Sample Input :
# 4 1 2 3 4     (1 is at front)
# Sample Output :
# 4 3 2 1    (4 is at front)


import queue
def reverseQueue(q1):
#### Implement Your Code Here
    q=[]
    while not q1.empty():
       q.append(q1.get())
    while len(q)>0:
        q1.put(q.pop())

from sys import setrecursionlimit
setrecursionlimit(11000)
li = [int(ele) for ele in (input().split()[1:])]
q1 = queue.Queue()
for ele in li:
    q1.put(ele)
reverseQueue(q1)
while(q1.empty() is False):
    print(q1.get(),end= ' ')