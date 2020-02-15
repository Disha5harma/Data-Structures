# Longest subset zero sum
# Send Feedback
# Given an array consisting of positive and negative integers, find the length of the longest continuous subset whose sum is zero.
# NOTE: You have to return the length of longest subset .
# Input Format :
# Line 1 : Contains an integer N i.e. size of array

# Line 2 : Contains N elements of the array, separated by spaces
# Output Format
#  Line 1 : Length of longest continuous subset 
# Sample Input :
# 10 
#  95 -97 -387 -435 -5 -70 897 127 23 284
# Sample Output :
# 5

def subsetSum(l):
    #m = {num:True for num in l}
    n = len(l)
    sum = [0] * n
    sum[0] = l[0]
    m = { l[0]:0}
    start, end = -1, -2
    if sum[0]==0:
        start, end = 0, 0
    for i in range(1, n):
        sum[i] = sum[i-1] + l[i]
        if sum[i]==0:
            start, end = 0, i
        elif sum[i] in m:
        # Found a subset with zero Sum
            if i-m[sum[i]] > end-start+1:
                start, end = m[sum[i]]+1, i
        else:
            m[sum[i]] = i
    return start, end
# Main 
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
start, end = subsetSum(l)
print(end-start+1)