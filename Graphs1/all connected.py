# Code : All connected components
# Send Feedback
# Given an undirected graph G(V,E), find and print all the connected components of the given graph G.
# V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
# E is the number of edges present in graph G.
# You need to take input in main and create a function which should return all the connected components. And then print them in the main, not inside function.
# Print different components in new line. And each component should be printed in increasing order (separated by space). Order of different components doesn't matter.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting that there exists an edge between Vertex 'a' and Vertex 'b'.
# Output Format :
# Different components in new line
# Constraints :
# 2 <= V <= 1000
# 1 <= E <= 1000
# Sample Input 1:
# 4 2
# 0 1
# 2 3
# Sample Output 1:
# 0 1 
# 2 3 
# Sample Input 2:
# 4 3
# 0 1
# 1 3 
# 0 3
# Sample Output 2:
# 0 1 3 
# 2



class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)]for j in range(nVertices)]
        
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
        
    def Isconnected(self):
            visited=[False for i in range(self.nVertices)]
            for i in range(self.nVertices):
                if visited[i] is False:
                    li = []
                    self.Isconnected__helper(i, visited, li)
                    li.sort()
                    print(*li)
                
    
    def Isconnected__helper(self, sv, visited, li):
        li.append(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] > 0 and visited[i] == False:
                self.Isconnected__helper(i, visited, li )
#main
v,e=(int(i) for i in input().split())
g=Graph(v)
while e:
    a,b=(int(i) for i in input().split())
    g.addEdge(a,b)
    e-=1
g.Isconnected()
