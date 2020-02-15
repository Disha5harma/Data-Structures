# Return subsets sum to K
# Send Feedback
# Given an array A of size n and an integer K, return all subsets of A which sum to K.
# Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.
# Note : The order of subsets are not important.
# Input format :
# Line 1 : Integer n, Size of input array
# Line 2 : Array elements separated by space
# Line 3 : K 
# Constraints :
# 1 <= n <= 20
# Sample Input :
# 9 
# 5 12 3 17 1 18 15 3 17 
# 6
# Sample Output :
# 3 3
# 5 1


def printAllSubsetsRec(arr, n, v, sum) : 
  
    # If remaining sum is 0, then print all 
    # elements of current subset. 
    #x=arr
    if (sum == 0) : 
#         if len(v)>1:
#             
#             #print(arr)
#             for value in arr:
#                     if value in v:
#                         x.append(value)
#             
        
#         else
        x=[]
        l=len(v)
        x1=l-1
        while(x1>=0):
            x.append(v[x1])
            #print(v[x1],end=" ")
            x1-=1
        print(*x,sep=" ")
        #print() 
        return
        
    # If no remaining elements, 
    if (n == 0): 
        return
  
    
    printAllSubsetsRec(arr, n - 1, v, sum) 
    v1 = [] + v 
    v1.append(arr[n - 1]) 
    printAllSubsetsRec(arr, n - 1, v1, sum - arr[n - 1]) 
  
  
# Wrapper over printAllSubsetsRec() 
def printAllSubsets(arr, n, sum): 
  
    v = [] 
    printAllSubsetsRec(arr, n, v, sum) 
  
  
# Driver code 
n = int(input())
arr=list(int(i) for i in input().strip().split(" "))
sum=int(input())
printAllSubsets(arr, n, sum) 