# K Smallest Elements
# Send Feedback
# You are given with an integer k and an array of integers that contain numbers in random order. Write a program to find k smallest numbers from given array. You need to save them in an array and return it.
# Time complexity should be O(nlogk) and space complexity should be not more than O(k).
# Order of elements in the output is not important.
# Input Format :
# Line 1 : Size of array (n)
# Line 2 : Array elements (separated by space)
# Line 3 : Integer k
# Output Format :
# k smallest elements
# Sample Input 1 :
# 13
# 2 12 9 16 10 5 3 20 25 11 1 8 6 
# 4
# Sample Output 1 :
# 5
# 3
# 2
# 1

import heapq
def kSmallest(arr, k):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    heap=arr[:k]
    heapq._heapify_max(heap)
    n=len(arr)
    for i in range(k,n):
        if heap[0]>arr[i]:
            heapq._heapreplace_max(heap,arr[i])
    return heap
    pass

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
for i in ans:
    print(i)
