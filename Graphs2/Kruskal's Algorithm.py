# Kruskal's Algorithm
# Send Feedback
# Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
# Find and print the Minimum Spanning Tree (MST) using Kruskal's algorithm.
# For printing MST follow the steps -
# 1. In one line, print an edge which is part of MST in the format -
# v1 v2 w
# where, v1 and v2 are the vertices of the edge which is included in MST and whose weight is w. And v1 <= v2 i.e. print the smaller vertex first while printing an edge.
# 2. Print V-1 edges in above format in different lines.
# Note : Order of different edges doesn't matter.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)
# Output Format :
# MST
# Constraints :
# 2 <= V, E <= 10^5
# Sample Input 1 :
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8
# Sample Output 1 :
# 1 2 1
# 0 1 3
# 0 3 5


class Edge:
    def __init__(self,src,dest,wt):
        self.src=src
        self.dest=dest
        self.wt=wt
    
def kruskal(edges,nvertices):
    parent=[i for i in range(nvertices)]
    edges=sorted(edges,key=lambda edge:edge.wt)
    count=0
    output=[]
    i=0
    while count<(nvertices-1):
        currentedge=edges[i]
        srcparent=getparent(currentedge.src,parent)
        destparent=getparent(currentedge.dest,parent)
        if srcparent!=destparent:
            output.append(currentedge)
            count+=1
            parent[srcparent]=destparent
        i+=1
    return output
def getparent(v,parent):
    if v==parent[v]:
        return v
    return getparent(parent[v],parent)
    
lst=[int(ele) for ele in input().split()]
n=lst[0]
e=lst[1]
edges=[]
for i in range(e):
    curr_input=[int(i) for i in input().split()]
    src=curr_input[0]
    dest=curr_input[1]
    wt=curr_input[2]
    edge=Edge(src,dest,wt)
    edges.append(edge)
output=kruskal(edges,n)
for i in output:
    if i.dest>i.src:
        print(i.src,i.dest,i.wt)
    else:
        print(i.dest,i.src,i.wt)