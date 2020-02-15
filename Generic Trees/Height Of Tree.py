# Height Of Tree
# Send Feedback
# Given a generic tree, find and return the height of given tree.
# Input format :
# Elements in level order form separated by space (as per done in class). Order is - 
# Root_data, n (No_Of_Child_Of_Root), n children, and so on for every element 
# Output Format :
# Height
# Sample Input :
# 10 3 20 30 40 2 40 50 0 0 0 0 
# Sample Output :
# 3

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()
        

def printTree(root):
    if root==None:
        return
    
    print(root.data)
    for child in root.children:
        printTree(child)
    return root
def height(root):
    m=0
    for ele in root.children:
        l1=height(ele)
        m=max(m,l1)
    return 1+m
def createLevelWiseTree(arr):
    root = TreeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = TreeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(height(tree))