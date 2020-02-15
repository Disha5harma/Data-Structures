# Kth largest element
# Send Feedback
# Given an array A of random integers and an integer k, find and return the kth largest element in the array.
# Try to do this question in less than O(nlogn) time.
# Input Format :
# Line 1 : An integer N i.e. size of the array
# Line 2 : N integers which are elements of the array, separated by spaces
# Line 3 : An integer k
# Output Format :
# kth largest element
# Input Constraints :
# 1 <= N, Ai, k <= 10^5
# Sample Input 1 :
# 6
# 9 4 8 7 11 3
# 2
# Sample Output 1 :
# 9
# Sample Input 2 :
# 8
# 2 6 10 11 13 4 1 20
# 4
# Sample Output 2 :
# 10

import heapq
def kthLargest(arr, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    n=len(arr)
    heapsort(arr)
    return arr[k-1]
def down_heapify(arr,i,n):
    parentIndex= i
    leftChildIndex=2*i+1
    rightChildIndex=2*i+2
    while leftChildIndex<n:
        minIndex=parentIndex
        if arr[minIndex]>arr[leftChildIndex]:
            minIndex=leftChildIndex
        if rightChildIndex<n and arr[minIndex]>arr[rightChildIndex]:
            minIndex=rightChildIndex
        if parentIndex==minIndex:
            return
        arr[minIndex],arr[parentIndex]=arr[parentIndex],arr[minIndex]
        parentIndex=minIndex
        leftChildIndex=parentIndex*2+1
        rightChildIndex=parentIndex*2+2
        
def heapsort(arr):
    n=len(arr)
    for i in range(n//2,-1,-1):
        down_heapify(arr,i,n)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        down_heapify(arr,0,i)
    return


# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)
