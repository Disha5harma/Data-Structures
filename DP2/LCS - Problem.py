LCS - Problem
Send Feedback
Given 2 strings of S1 and S2 with lengths m and n respectively, find the length of longest common subsequence.
A subsequence of a string S whose length is n, is a string containing characters in same relative order as they are present in S, but not necessarily contiguous. Subsequences contain all the strings of length varying from 0 to n. E.g. subsequences of string "abc" are - "",a,b,c,ab,bc,ac,abc.
Input Format :
Line 1 : String S1
Line 2 : String s2
Output Format :
Line 1 : Length of lcs
Sample Input :
adebc
dcadb
Sample Output :
3


def lcsDP(s1,s2):
        n=len(s1)
        m=len(s2)
        dp=[[0 for j in range(m+1)] for i in range(n+1)]
#Implement Your Code Here
#         if i==len(s1) or j==len(s2):
#             return 0
    
#         if s1[i]==s2[j]:
#             if dp[i+1][j+1]==-1:
#                 smallans=1+lcsDP(s1,s2,i+1,j+1,dp)
#                 dp[i+1][j+1]=smallans
#                 ans=1+smallans
#             else:
#                 ans=1+dp[i+1][j+1]
#         else:
#             if dp[i+1][j]==-1:
#                 ans1=lcsDP(s1,s2,i+1,j,dp)
#                 dp[i+1][j]=ans1
#             else:
#                 ans1=dp[i+1][j]
                
#             if dp[i][j+1]==-1:
#                 ans2=lcsDP(s1,s2,i,j+1,dp)
#                 dp[i][j+1]=ans2
                
#             else:
#                 ans2=dp[i][j+1]
                
#             ans=max(ans1,ans2)
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                
                if s1[i]==s2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
#         if s1[i]==s2[j]:
#             if dp[i+1][j+1]==1:
#                 smallans=1+lcs(s1,s2,i+1,j+1)
#                 dp[i+1][j+1]=smallans
#                 ans=1+smallans
#             else:
#                 ans=1+dp[i+1][j+1]
#         else:
#             if dp[i][j+1]==-1:
#                 ans2=lcsDP(s1,s2,i,j+1)
#                 dp[i][j+1]=ans2
#             else:
#                 ans2=dp[i][j+1]
         
#             if dp[i+1][j]==-1:
#                 ans1=lcsDP(s1,s2,i+1,j)
#                 dp[i+1][j]=ans1
#             else:
#                 ans1=dp[i+1][j]
#             ans=max(ans1,ans2)
#         return ans
        
        pass



s1 =input().strip()
s2 =input().strip()

print(lcsDP(s1, s2))