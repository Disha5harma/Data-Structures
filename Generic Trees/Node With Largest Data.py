# Node With Largest Data
# Send Feedback
# Given a generic tree, find and return the node with maximum data. You need to return the complete node which is having maximum data.
# Return null if tree is empty.
# Input format :
# Elements in level order form separated by space (as per done in class). Order is - 
# Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
# Output Format :
# Node with largest data
# Sample Input :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# Sample Output :
# 50

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def maxDataNode(tree):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if tree==None:
        return 0
    max=tree.data
    for ele in tree.children:
        curr=maxDataNode(ele)
        if curr.data>max:
            max=curr
    return max
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
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(maxDataNode(tree))