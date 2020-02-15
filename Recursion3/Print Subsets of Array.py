# Print Subsets of Array
# Send Feedback
# Given an integer array (of length n), find and print all the subsets of input array.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Note : The order of subsets are not important. Just print the subsets in different lines.
# Input format :
# Line 1 : Integer n, Size of array
# Line 2 : Array elements (separated by space)
# Constraints :
# 1 <= n <= 15
# Sample Input:
# 3
# 15 20 12
# Sample Output:
# [] (this just represents an empty array, don't worry about the square brackets)
# 12 
# 20 
# 20 12 
# 15 
# 15 12 
# 15 20 
# 15 20 12 


def subsetsUtil(A, subset, index): 
    print(*subset) 
    for i in range(index, len(A)):  
          
        # include the A[i] in subset.  
        subset.append(A[i]) 
          
        # move onto the next element.  
        subsetsUtil(A,subset, i + 1)  
          
        # exclude the A[i] from subset and  
        # triggers backtracking. 
        subset.pop(-1)  
    return
  
# below function returns the subsets of vector A.  
def subsets(A): 
    global res 
    subset = [] 
      
    # keeps track of current element in vector A  
    index = 0
    subsetsUtil(A, subset, index) 
# Driver Code 
n=int(input())
arr=list(int(i) for i in input().strip().split(" "))
#n = len(arr) 
subsets(arr)