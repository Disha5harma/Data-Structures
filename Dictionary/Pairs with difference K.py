# Pairs with difference K
# Send Feedback
# You are given with an array of integers and an integer K. Write a program to find and print all pairs which have difference K.
# Best solution takes O(n) time. And take difference as absolute.
# Input Format :
# Line 1 : Integer n, Size of array
# Line 2 : Array elements (separated by space)
# Line 3 : K
# Output format :
# Print pairs in different lines (pair elements separated by space). In a pair, smaller element should be printed first.
# (Order of different pairs is not important)
# Constraints :
# 1 <= n <= 5000
# Sample Input 1 :
# 4 
# 5 1 2 4
# 3
# Sample Output 1 :
# 2 5
# 1 4
# Sample Input 2 :
# 4
# 4 4 4 4 
# 0
# Sample Output 2 :
# 4 4
# 4 4
# 4 4
# 4 4
# 4 4
# 4 4


def printPairDiffK(l, k):
#Implement Your Code Here
    dict={}
    for ele in l:
        dict[ele]=dict.get(ele,0)+1
    for i in l:
        c=0
        d=0
        if k==0:
            while d<((dict[i])*(dict[i]-1)/2):
                print(i,i)
                d+=1
        else:
            if i+k in dict:

                    while c<(dict[i]*dict[i+k]):
                        print(i,i+k)
                        c+=1
            if i-k in dict:

                    while d<(dict[i]*dict[i-k]):
                            print(i-k,i)
                            d+=1
        dict[i]=0
            
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
printPairDiffK(l, k)