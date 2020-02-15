
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# def take_input():
    
#     inputlist=[int(i) for i in input().split()]
#     head=None
#     for currd in inputlist:
#         if currd==-1:
#             break
#         newnode=Node(currd)
#         if head is None:
#             head=newnode
#         else:
#             curr=head
#             while curr.next is not None:
#                 curr=curr.next
#             curr.next=newnode
#     return head
# def print_list(head):
#     while head is not None:
#         print(head.data,"->",end="")
#         head=head.next
#     print("None")
    
# head=take_input()
# print_list(head)    


#OPTIMIZED METHOD

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# def inputl():
    
#     mylist=[int(i) for i in input().split()]
#     head=None
#     tail=None
#     for currd in mylist:
#         if currd==-1:
#             break
#         newnode=Node(currd)
#         if head is None:
#             head=newnode
#             tail=newnode
#         else:
#             tail.next=newnode
#             tail=newnode
#     return head

# def knapsack(W,val,wt):
#     n=len(val)
#     dp=[[0 for j in range(W+1)] for i in range(n+1)]

#     for i in range(1,n+1):
#         for j in range(1,W+1):
#             if j<wt[i-1]:
#                 ans=dp[i-1][j]
#             else:
#                 ans1=val[i-1][j-wt[i-1]]
#                 ans2=dp[i-1][j]
#                 ans=max(ans1,ans2)
#             dp[i][j]=ans

#     return dp[n][W]
    
#     pass

# from sys import setrecursionlimit
# setrecursionlimit(11000)
# n=int(input())
# weights=list(int(i) for i in input().strip().split(''))
# values=list(int(i) for i in input().strip().split(''))
# maxWeight=int(input())
# print(knapsack( maxWeight, values,weights))

# def knapsack(W,val,wt,n,i):
#     if i==n:
#         return 0

#     if wt[i]>W:
#         ans=knapsack(W,val,wt,n,i+1)
#     else:
#         ans1=val[i]+knapsack(W-wt[i],val,wt,n,i+1)
#         ans2=knapsack(W,val,wt,n,i+1)
#         ans=max(ans1,ans2)
#     return ans

def mcm(p,i,j,dp):

    if i==j:
        return 0
    min_value=sys.maxsize
    for k in range(i,j):
        if dp[i][k]==-1:
            ans1=mcm(p,i,k,dp)
            dp[i][k]=ans1
        else:
            ans1=dp[i][k]
        if dp[k+1][j]==-1:
            ans2=mcm(p,k+1,j,dp)
            dp[k+1][j]=ans2
        else:
            ans2=dp[k+1][j]

        mCost=[i-1]*p[k]*p[j]
        curr_value=ans1+ans2+mCost
        min_value=min(min_value,curr_value)
        print(min_value)
    return min_value

    p=[1,2,3,4,5,6]
    n=len(p)-1
    dp=[[-1 for j in range(n+1)] for i in range(n+1)]
    ans=mcm(p,1,n,dp)
    print(ans)