# Return subset of an array
# Send Feedback
# Given an integer array (of length n), find and return all the subsets of input array.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Note : The order of subsets are not important.
# Input format :

# Line 1 : Size of array

# Line 2 : Array elements (separated by space)

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

def printPowerSet(arr, n): 
      
    # Function to find all subsets of given set. 
    # Any repeated subset is considered only  
    # once in the output 
    _list = [] 
    for i in range(2**n): 
        subset = "" 
  
        # consider each element in the set 
        for j in range(n): 
  
            # Check if jth bit in the i is set.  
            # If the bit is set, we consider  
            # jth element from set 
            if (i & (1 << j)) != 0: 
                subset += str(arr[j]) + "|"
         
        # if subset is encountered for the first time 
        # If we use set<string>, we can directly insert 
        if subset not in _list and len(subset) > 0: 
            _list.append(subset) 
    for subset in _list: 
        arr = subset.split('|') 
        for string in arr: 
            print(string,end =" ") 
        print()
  
# Driver Code 
n=int(input())
arr=list(int(i) for i in input().strip().split(" "))
#n = len(arr) 
_list=printPowerSet(arr, n)
