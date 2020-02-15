# Reverse first K elements

# Given a queue and an integer k, reverse first k elements. Return the updated queue.
# Do the problem in O(n) complexity.
# Input Format :
# Line 1 : Integer N, Size of Queue
# Line 2 : Queue Elements (separated by space)
# Line 3 : Integer k
# Output Format:
# Updated Queue elements
# Contraints :
# 1<= N <=10000
# Sample Input 1:
# 5
# 1 2 3 4 5
# 3
# Sample Output 1:
# 3 2 1 4 5
# Sample Input 2:
# 7
# 3 4 2 5 6 7 8
# 7
# Sample Output 2:
# 8 7 6 5 2 4 3


import queue
def reverseFirstK(q,k):
#Implement Your Code Here  
    l=[]
    i=0
    q1=queue.Queue()
    c=q.qsize()
    while i<k:
        l.append(q.get())
        i+=1
    while len(l)>0:
        q.put(l.pop())
    for j in range(c-k):
        q1.put(q.get())
    j=c-k-1   
    while j>=0:
        q.put(q1.get())
        j-=1
        
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
	q.put(ele)
k = int(input())
reverseFirstK(q,k) 
while(q.qsize()>0):
	print(q.get())
	n-=1