# Code : Is Connected ?
# Send Feedback
# Given an undirected graph G(V,E), check if the graph G is connected graph or not.
# V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
# E is the number of edges present in graph G.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting that there exists an edge between Vertex 'a' and Vertex 'b'.
# Output Format :
# "true" or "false"
# Constraints :
# 2 <= V <= 1000
# 1 <= E <= 1000
# Sample Input 1:
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# Sample Output 1:
# true
# Sample Input 2:
# 4 3
# 0 1
# 1 3 
# 0 3

class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)]for j in range(nVertices)]
        
    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
        
    def Isconnected(self):
        visited=[False for i in range(self.nVertices)]
        self.Isconnected__helper(0,visited)
        for i in visited:
            if i==False:
                return False
        return True
    
    def Isconnected__helper(self,sv,visited):
        visited[0]=True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i]>0 and visited[i]==False:
                visited[i]=True
                self.Isconnected__helper(i,visited)
#main
v,e=(int(i) for i in input().split())
g=Graph(v)
while e:
    a,b=(int(i) for i in input().split())
    g.addEdge(a,b)
    e-=1
if(g.Isconnected()==True):
    print('true')
else:
    print('false')
            