#Find unique element
def FindUnique(arr):
    # Please add your code here
    s=arr[0]
    l=len(arr)
    for i in range(1,l):
       s=s^arr[i]
    return s
    pass

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
unique=FindUnique(arr)
print(unique)


#Duplicate in array
def MissingNumber(arr):
    # Please add your code here
    l=len(arr)
    s1=0
    for i in range(l-1):
        s1+=i
    s=0
    
    for i in range(l):
        s+=arr[i]
    return s-s1
    pass

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
ans=MissingNumber(arr)
print(ans)


def bsort(arr):
    l=len(arr)
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
# Pair sum in array
# Sample Input:
# 9
# 1 3 6 2 5 4 3 2 4
# 7
# Sample Output :
# 1 6
# 3 4
# 3 4
# 2 5
# 2 5
# 3 4
# 3 4

def pairSum(arr,x):
    l=len(arr)
    bsort(arr)
    n=l//2
    i=0
    j=l-1
    p=0
    while(i<j):
        s=arr[i]+arr[j]
        if s>x:
            j-=1
        elif s<x:
            i+=1
        else:
            c=0
            if arr[i]==arr[j]:
                c=j-i+1
                p=(c*(c-1))//2
                i=j
            else:
                sc=1
                ec=1
                while i+1<j and arr[i]==arr[i+1]:
                    sc+=1
                    i+=1
                while i<j-1 and arr[j]==arr[j-1]:
                    ec+=1
                    j-=1
                p=sc*ec
                
            for k in range(p):
                print(arr[i],arr[j])
            i+=1
            j-=1
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())


# Rotate array
# Given a random integer array of size n, write a function that rotates the given array by d elements (towards left)
# Change in the input array itself. You don't need to return or print elements.
# Sample Input :
# 7
# 1 2 3 4 5 6 7
# 2
# Sample Output :
# 3 4 5 6 7 1 2

def Rotate(arr, d):
    # Please add your code here
    l=len(arr)
    sarr=arr[:d]
    j=0
    for i in range(d,l):
        arr[j]=arr[i]
        j+=1
    
    for i in range(d):
       # arr[l-d+i]=sarr[i]
        arr[j]=sarr[i]
        j+=1
        
    pass


# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
d=int(input())
Rotate(arr, d)
print(*arr)