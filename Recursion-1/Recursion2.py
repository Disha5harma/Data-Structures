# Remove X
# Given a string, compute recursively a new string where all 'x' chars have been removed.
# Sample Input 1 :
# xaxb
# Sample Output 1:
# ab
# def removeX(string):
#     l=len(string)
#     if l==0:
#         return string
#     sarr=string[1:]
#     if string[0]!='x':
#         return string[0]+removeX(sarr)
#     else:
#         return removeX(sarr)
#     pass

# # Main
# string = input()
# print(removeX(string))
def removeConsecutiveDuplicates(string):
    # Please add your code here
    if len(string)<=1:
    	return string
    string2=removeConsecutiveDuplicates(string[1:])
    if string[0]==string[1]:
    	return string2
    else:
    	return string[0]+string2
# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))

#BINARY SEARCH BY RECURSION
def binarysearch(a,x,ei,si):
	if si>ei:
		return -1

	mid=(si+ei)//2
	if a[mid]==x:
		return mid
	elif a[mid]>x:
		return binarysearch(a,x,mid-1,si)
	else:
		return binarysearch(a,x,ei,mid+1)


#MERGE SORT BY RECURSION
def merge(arr1,arr2,arr):
    i=0
    j=0
    k=0
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]>arr2[j]:
            arr[k]=arr2[j]
            j+=1
            k+=1
        else:
            arr[k]=arr1[i]
            i+=1
            k+=1
    while(i<len(arr1)) :
            arr[k]=arr1[i]
            i+=1
            k+=1
    while(j<len(arr2)) :
            arr[k]=arr2[j]
            j+=1
            k+=1
    

def mergeSort(arr, start, end):
    # Please add your code here
    l=len(arr)
    if l==0 or l==1:
        return arr
    mid=(start+end)//2
    a1=arr[:mid]
    a2=arr[mid:]
    mergeSort(a1,0,len(a1))
    mergeSort(a2,0,len(a2))
    merge(a1,a2,arr)
    pass

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr, 0, n)
print(*arr)

#QUICK SORT WITH RECURSION

def partition(arr,si,ei):
    
    pivot=arr[si]
    c=0
    for i in range(si,ei+1):
        if pivot>arr[i]:
            c+=1
    arr[si],arr[si+c]=arr[si+c],arr[si]
    pivotindex=si+c
    i=si
    j=ei
    while(i<j):
        if arr[i]<pivot:
            i+=1
        elif arr[j]>=pivot:
            j-=1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
            
    return pivotindex


def quickSort(arr,si,ei):
    if si>=ei:
        return 
    pivotindex=partition(arr,si,ei)
    
    quickSort(arr,si,pivotindex-1)
    quickSort(arr,pivotindex+1,ei)
    
    pass

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
quickSort(arr, 0, n-1)
print(*arr)

#TOWER OF HANOI
# Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move all disks from source rod to destination rod using third rod (say auxiliary). The rules are :
# 1) Only one disk can be moved at a time.
# 2) A disk can be moved only if it is on the top of a rod.
# 3) No disk can be placed on the top of a smaller disk.
# Print the steps required to move n disks from source rod to destination rod.
# Source Rod is named as 'a', auxiliary rod as 'b' and destination rod as 'c'.
# Sample Input :
# 2
# Sample Output :
# a b
# a c
# b c
def towerofhanoi(n, source, aux, dest):
    # Please add your code here
    if n<=0:
        return
    towerofhanoi(n-1,source,dest,aux)
    print(source,dest)
    towerofhanoi(n-1,aux,source,dest)
    pass

n=int(input())
towerofhanoi(n, 'a', 'b', 'c')

# Multiplication (Recursive)
# Send Feedback
# Given two integers m & n, calculate 
# and return their multiplication using recursion. You can only use subtraction and addition for your calculation.
# No other operators are allowed.
# Sample Input :
# 3 
# 5
# Sample Output -
# 15
def multi(m,n):
    
    if n==0 or m==0:
        return 0
    
    return m+multi(m,n-1)

m=int(input(""))
n=int(input(""))
print(multi(m,n))

# Geometric Sum
# Send Feedback
# Given k, find the geometric sum i.e.
# 1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
# using recursion. Return the answer.
# Sample Input :
# 3
# Sample Output :
# 1.875
def geosum(n):
    if n==0:
        return 1
    return pow(0.5,n)+geosum(n-1)

n=int(input(""))
output=geosum(n)
print('%.5f'%output)

# Check Palindrome (recursive)
# Sample Input 1 :
# racecar
# Sample Output 1:
# true

def palindrome(arr,si,ei):
    l=len(arr)
    if si>=ei:
        return True
    
    if arr[si]!=arr[ei]:
        return False
    
    return palindrome(arr,si+1,ei-1)

arr=input("")
output=palindrome(arr,0,len(arr)-1)
if output==True:
    print('true')
else:
    print('false')

# Sum of digits (recursive)

# Write a recursive function that returns the sum of the digits of a given integer.
# Sample Input :
# 12345
# Sample Output :
# 15
def sumofdigits(n):
	if n==0:
		return 0
	smallans=sumofdigits(n//10)
	return smallans+n%10

n=int(input())
print(sumofdigits(n))

#String to Integer
# Write a recursive function to convert a given string into the
# number it represents. That is input will be a numeric string 
# that contains only numbers, you need to convert the string 
# into corresponding integer and return the answer.
def convert(string):
    l=len(string)
    if l==1:
        return ord(string[l-1])-48
    sarr=string[1:]
    n=ord(string[0])-48
    
    
    return convert(sarr) + n*(pow(10,l-1))

string=input("")
print(convert(string))

# Pair star
# Send Feedback
# Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
# Sample Input 1 :
# hello
# Sample Output 1:
# hel*lo
# Sample Input 2 :
# xxyy
# Sample Output 2:
# x*xy*y
def pairstar(arr):
    l=len(arr)
    x='*'
    if l==0 or l==1:
        return arr
    if arr[0]==arr[1]:
        sarr=arr[2:]
        return arr[0]+x+pairstar(arr[1]+sarr)
    else:
        sarr=arr[1:]
        return arr[0]+pairstar(sarr)
    
arr=input("")
print(pairstar(arr))

# Staircase
# A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. 
# Implement a method to count how many possible ways the child can run up to the stairs.
#  You need to return number of possible ways W.
# Sample Input 1:
# 4
# Sample Output :
# 7
def staircase(n):
    if n==1 or n==2:
        return n
    if n<=0:
        return 1
    x=staircase(n-1)
    y=staircase(n-2)
    z=staircase(n-3)
    
    return x+y+z

n=int(input(''))
print(staircase(n))


