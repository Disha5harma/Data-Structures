# Node with maximum child sum
# Send Feedback
# Given a tree, find and return the node for which sum of data of all children and the node itself is maximum. In the sum, data of node itself and data of immediate children is to be taken.
# Input format :
# Line 1 : Elements in level order form separated by space (as per done in class). Order is - 
# Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
# Output format :
# Node with maximum sum.
# Sample Input 1 :
# 5 3 1 2 3 1 15 2 4 5 1 6 0 0 0 0
# Sample Output 1 :
# 1


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)
maxNode=None
maxData=-10000000000
def maxSumNode(tree):
    # Return the node and its sum
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    global maxData,maxNode
    if tree.children==[]:
        if tree.data>maxData:
            maxNode=tree
            maxData=0
            return tree,0
    sum=tree.data
    for child in tree.children:
        sum+=child.data
    if sum>=maxData:
        maxData=sum
        maxNode=tree
    for child in tree.children:
        maxSumNode(child)
    return maxNode,maxData

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
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
ans,sum=maxSumNode(tree)
print(ans)
