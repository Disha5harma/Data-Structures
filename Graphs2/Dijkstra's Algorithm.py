# Dijkstra's Algorithm
# Send Feedback
# Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
# Find and print the shortest distance from the source vertex (i.e. Vertex 0) to all other vertices (including source vertex also) using Dijkstra's Algorithm.
# Print the ith vertex number and the distance from source in one line separated by space. Print different vertices in different lines.
# Note : Order of vertices in output doesn't matter.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)
# Output Format :
# In different lines, ith vertex number and its distance from source (separated by space)
# Constraints :
# 2 <= V, E <= 10^5
# Sample Input 1 :
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8
# Sample Output 1 :
# 0 0
# 1 3
# 2 4
# 3 5

import sys
class edge:
    def __init__(self,s,d,w):
        self.s=s
        self.d=d
        self.w=w

def prims(edges,visited,nVertices):
    adjMatrix=[[99999 for i in range(nVertices)]for j in range(nVertices)]
    for e in edges:
        adjMatrix[e.s][e.d]=adjMatrix[e.d][e.s]=e.w
    par=[0 for i in range(nVertices)]
    dist=[adjMatrix[0][x] for x in range(nVertices)]
    output=[]
    dist[0]=0
    v=0
    visited[0]=1
    count=nVertices-1
    while count:
        min=99999
        for i in range(nVertices):
            if not visited[i] and dist[i]<min:
                min=dist[i]
                v=i
        visited[v]=1
        u=par[v]
        output.append(edge(u,v,adjMatrix[u][v]))
        for i in range(nVertices):
            if not visited[i] and adjMatrix[v][i]  and dist[i]>dist[v]+adjMatrix[v][i]:
                par[i]=v
                dist[i]=dist[v]+adjMatrix[v][i]
        count-=1
    return dist
        

edges=[]
nVertices,nEdges=[int(x) for x in input().split()]
for i in range(nEdges):
    s,d,w=[int(x) for x in input().split()]
    edges.append(edge(s,d,w))
    
visited=[0 for i in range(nVertices)]
output=prims(edges,visited,nVertices)

for i in range(len(output)):
    print(i,output[i])