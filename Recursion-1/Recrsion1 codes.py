#POWER OF A NUMBER
# Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
# Input format :
# Two integers x and n (separated by space)
# Output Format :
# x^n (i.e. x raise to the power n)
# Sample Input 1 :
#  3 4
# Sample Output 1 :
# 81
# def powerofnum(num,p):
# 	if p==1:
# 		return num
# 	return num*powerofnum(num,p-1)

# arr=list(int(i) for i in input().strip().split(" "))
# num=arr[0]
# p=arr[1]
# print(powerofnum(num,p))

#FIBONNACI SERIES
#Sample Input 1 :
#  4
# Sample Output 1 :
# 3
#explanation:
# 1
# 1
# 2
# 3 <- last number of fibo series
# def fibos(num):
# 	if num==1 or num==2:
# 		return 1
# 	fib_1=fibos(num-1)
# 	fib_2=fibos(num-2)
# 	return fib_1+fib_2

# num=int(input())
# print(fibos(num))

# CHECK FOR SORTED OR NOT

# def ifsorted(arr):
# 	if len(arr)==1:
# 		return True
# 	if arr[0]>arr[1]:
# 		return False
# 	return ifsorted(arr[1:])

# arr=list(int(i) for i in input().strip().split(" "))
# print(ifsorted(arr))

#CHECK FOR SORTED OR NOT
#BETTER VERSION FOR CHECKING WITHOUT SLICING THE ARRAY
# def ifsortedbetter(arr,si):
# 	n=len(arr)
# 	if si==n-1:
# 		return True
# 	if arr[si]>arr[si+1]:
# 		return False
# 	return ifsortedbetter(arr,si+1)

# arr=list(int(i) for i in input().strip().split(" "))
# print(ifsortedbetter(arr,0))
#SUM OF ARRAY
# def sumArray(arr):
#      # Please add your code here
#     l=len(arr)
#     if l==1:
#         return arr[0]
#     sarr = arr[1:]
#     return arr[0] + sumArray(sarr)

# arr=list(int(i) for i in input().strip().split(" "))
# print(sumArray(arr))

# First Index of Number
# Sample Input :
# 4
# 9 8 10 8
# 8
# Sample Output :
# 1
# def firstIndex(arr, x):
#     # Please add your code here
#     l = len(arr)
#     if l==0 :
#         return -1
#     if arr[0]==x:
#         return 0
#     sarr = arr[1:]
#     soutput = firstIndex(sarr,x)
#     if soutput==-1:
#         return -1
#     else:
#         return soutput + 1
    
#     pass

# # Main
# from sys import setrecursionlimit
# setrecursionlimit(11000)
# arr=list(int(i) for i in input().strip().split(' '))
# x=int(input())
# print(firstIndex(arr, x))

# def firstindexb(arr,x,si):
# 	l=len(arr)
# 	if si==l:
# 		return 
# 	if arr[si]==x:
# 		return si
# 	return firstindexb(arr,x,si+1)
# arr=list(int(i) for i in input().strip().split(' '))
# x=int(input())
# print(firstindexb(arr, x,0))

# # Last Index Of Number Question
# # Sample Input :
# # 4
# # 9 8 10 8
# # 8
# # Sample Output :
# # 3

# def lastIndex(arr,x):
#     l=len(arr)
#     if l==0:                                
#         return -1
#     sarr=arr[1:]
#     soutput=lastIndex(sarr,x)
#     if soutput!=-1:
#         return soutput+1
#     else:
#         if arr[0]==x:
#             return 0
#         else:
#             return -1
        
# arr=list(int(i) for i in input().strip().split(' '))
# x=int(input())
# print(lastIndex(arr, x))
