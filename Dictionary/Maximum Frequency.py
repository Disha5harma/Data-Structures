# Maximum Frequency
# Send Feedback
# You are given with an array of integers that contain numbers in random order. Write a program to find and return the number which occurs maximum times in the given input.
# If more than one element occurs same number of times in the input, return the element which is present in the input first.
# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Output Format :
# Most frequent element
# Constraints :
# 1 <= N <= 10^5
# Sample Input 1 :
# 13
# 2 12 2 11 12 2 1 2 2 11 12 2 6 
# Sample Output 1 :
# 2
# Sample Input 2 :
# 3
# 1 4 5


def maxFreq(l):
    # Please add your code here
    x=None
    d={}    
    for w in l:
        d[w]=d.get(w,0)+1
    m=max(d.values())
    for i in l:
        #print(i,end=" ")
        if d[i]==m:
            x=i
            break
    return x
    pass


# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))
