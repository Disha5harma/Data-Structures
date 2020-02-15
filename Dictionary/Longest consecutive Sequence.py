# Longest consecutive Sequence

# You are given with an array of integers that contain numbers in random order. Write a program to find the longest possible sub sequence of consecutive numbers using the numbers from given array.
# You need to return the output array which contains consecutive elements. Order of elements in the output is not important.
# Best solution takes O(n) time.
# If two sequences are of equal length then return the sequence starting with the number whose occurrence is earlier in the array.
# Input Format :
# Line 1 : Integer n, Size of array
# Line 2 : Array elements (separated by space)
# Constraints :
# 1 <= n <= 50000
# Sample Input 1 :
# 13
# 2 12 9 16 10 5 3 20 25 11 1 8 6 
# Sample Output 1 :
# 8 
# 9 
# 10 
# 11 
# 12
# Sample Input 2 :
# 7
# 15 13 23 21 19 11 16
# Sample Output 2 :
# 15 
# 16

def longestConsecutiveSubsequence(l):
    m=max(l)
    lst=[-1]*(m+1)
    for ele in l:
       lst[ele]=ele
    maxVal=0
    maxIndex=0
    for i in range(m+1):
        temp=0
        while i<=m and lst[i]!=-1:
            temp+=1
            i+=1
        else:
            i-=1
        if temp>=maxVal:
            if temp==maxVal and temp!=0:
                tIndex=i-temp+1
                if l.index(lst[tIndex])<l.index(lst[maxIndex]):
                    maxVal=temp
                    maxIndex=i-temp+1
            else:
                maxVal=temp
                maxIndex=i-temp+1
    final=lst[maxIndex:maxIndex+maxVal]
    return final
#Implement Your Code Here
#You have To Return the list of longestConsecutiveSubsequence


n=int(input())
l=list(int(i) for i in input().strip().split(' '))
final = longestConsecutiveSubsequence(l)
for num in final:
    print(num)

CORRECT SOL-IN FIG