# Min Cost Path Problem
# Send Feedback
# Given an integer matrix of size m*n, you need to find out the value of minimum cost to reach from the cell (0, 0) to (m-1, n-1).
# From a cell (i, j), you can move in three directions : (i+1, j), (i, j+1) and (i+1, j+1).
# Cost of a path is defined as the sum of values of each cell through which path passes.
# Input Format :
# Line 1 : Two integers, m and n
# Next m lines : n integers of each row (separated by space)
# Output Format :
# Minimum cost
# Constraints :
# 1 <= m, n <= 20
# Sample Input 1 :
# 3 4
# 3 4 1 2
# 2 1 8 9
# 4 7 8 1
# Sample Output 1 :
# 13


import sys
def mincost(cost,i,j,n,m):
    if i==n-1 and j==m-1:
        return cost[i][j]
    
    if i>=n or j>=m:
        return sys.maxsize
    
    ans1=mincost(cost,i,j+1,n,m)
    ans2=mincost(cost,i+1,j,n,m)
    ans3=mincost(cost,i+1,j+1,n,m)
    
    ans=cost[i][j]+min(ans1,ans2,ans3)
    
    return ans

x=[int(ele) for ele in input().split()]
row_num=x[0]
col_num=x[1]
#arr=[int(ele) for ele in input().split()]

# for i in x:
#     for 


# for i in range(n):
#     sarr=[]
#     for j in range(m-1):
#         p=larr[0]
#         larr.remove(p)
#         sarr.append(p)
#     cost.append(sarr)
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
#i=0
try:
    for row in range(row_num):
        i=0
        larr=[int(ele) for ele in input().split()]
        for col in range(col_num):
            multi_list[row][col]= larr[i]
            i+=1
    #print(multi_list)
    print(mincost(multi_list,0,0,row_num,col_num))
except EOFError:
    cost=[]
# for i in x:
#     for 
    larr=[int(ele) for ele in input().split(" ")]

    for i in range(n):
        sarr=[]
        for j in range(m-1):
            p=larr[0]
            larr.remove(p)
            sarr.append(p)
        cost.append(sarr)
# for i in x:
#     for 
# 
# print(larr)
# for i in range(n):
#     sarr=[]
#     for j in range(m-1):
#         p=larr[0]
#         larr.remove(p)
#         sarr.append(p)
#     cost.append(sarr)

#print(cost)

# 