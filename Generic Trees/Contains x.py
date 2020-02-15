# Contains x
# Send Feedback
# Given a generic tree and an integer x, check if x is present in the given tree or not. Return true if x is present, return false otherwise.
# Input format :
# Line 1 : Integer x
# Line 2 : Elements in level order form separated by space (as per done in class). Order is - 
# Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
# Output format :
# true or false
# Sample Input 1 :
# 40
# 10 3 20 30 40 2 40 50 0 0 0 0 
# Sample Output 1 :
# true
# Sample Input 2 :
# 4
# 10 3 20 30 40 2 40 50 0 0 0 0 
# Sample Output 2:
# false

import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def search(root,x):
    if root.data==x:
        return True
    for ele in root.children:
        search(ele,x)
    return root
    pass

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
x=int(input())
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
if search(tree,x):
    print('true')
else:
    print('false')