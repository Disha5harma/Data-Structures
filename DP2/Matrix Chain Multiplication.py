# Matrix Chain Multiplication
# Send Feedback
# Given a chain of matrices A1, A2, A3,.....An, you have to figure out the most efficient way to multiply these matrices i.e. determine where to place parentheses to minimise the number of multiplications.
# You will be given an array p[] of size n + 1. Dimension of matrix Ai is p[i - 1]*p[i]. You need to find minimum number of multiplications needed to multiply the chain.
# Input Format :
# Line 1 : Integer n i.e. number of matrices
# Line 2 : n + 1 integers i.e. elements of array p[] 
# Output Format :
# Line 1 : Minimum number of multiplication needed
# Constraints :
# 1 <= n <= 100
# Sample Input 1 :
# 3
# 10 15 20 25
# Sample Output :
# 8000
# Sample Output Explanation :
# There are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.
# If multiply in order A1*(A2*A3) then number of multiplications required are 15000.
# If multiply in order (A1*A2)*A3 then number of multiplications required are 8000.
# Thus minimum number of multiplications required are 8000

import sys
def mcm(p,n):
    dp = [[0 for j in range(n+1)] for i in range(n+1)]
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j=i+l-1
            dp[i][j] = sys.maxsize
            for k in range(i,j):
                mCost = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j] 
                if mCost < dp[i][j]:
                    dp[i][j] = mCost
    return dp[1][n]

n=int(input())
p=[int(x) for x in input().split()]
ans=mcm(p,n)
print(ans)
