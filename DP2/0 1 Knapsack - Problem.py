# 0 1 Knapsack - Problem
# Send Feedback
# A thief robbing a store and can carry a maximal weight of W into his knapsack. There are N items and ith item weigh wi and is value vi. What is the maximum value V, that thief can take ?
# Input Format :
# Line 1 : N i.e. number of items
# Line 2 : N Integers i.e. weights of items separated by space
# Line 3 : N Integers i.e. values of items separated by space
# Line 4 : Integer W i.e. maximum weight thief can carry
# Output Format :
# Line 1 : Maximum value V
# Constraints
# 1 <= N <= 20
# 1<= wi <= 100
# 1 <= vi <= 100
# Sample Input 1 :
# 4
# 1 2 4 5
# 5 4 8 6
# 5
# Sample Output :
# 13


def knapsack(W,val,wt,n,i):
    if i==n:
        return 0

    if wt[i]>W:
        ans=knapsack(W,val,wt,n,i+1)
    else:
        ans1=val[i]+knapsack(W-wt[i],val,wt,n,i+1)
        ans2=knapsack(W,val,wt,n,i+1)
        ans=max(ans1,ans2)
    return ans
    pass

from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
weights=list(int(i) for i in input().strip().split(' '))
values=list(int(i) for i in input().strip().split(' '))
maxWeight=int(input())
print(knapsack( maxWeight, values,weights,n,0))