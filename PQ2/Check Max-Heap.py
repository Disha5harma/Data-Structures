# Check Max-Heap
# Send Feedback
# Given an array of integers, check whether it represents max-heap or not.
# Return true or false.
# Input Format :
# Line 1 : An integer N i.e. size of the array
# Line 2 : N integers which are elements of the array, separated by spaces
# Output Format :
# true if it represents max-heap and false if it is not a max-heap
# Constraints :
# 1 <= N <= 10^5
# 1 <= Ai <= 10^5


def checkMaxHeap(lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    for i in range(len(lst)):
        l = 2*i+1
        r = 2*i+2
        
        if l<len(lst) and lst[l] > lst[i]:
            return False
        if r<len(lst) and lst[r] > lst[i]:
            return False
    return True

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
