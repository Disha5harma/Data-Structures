# Print nodes at distance k from node
# Send Feedback
# Given a binary tree, a node and an integer K, print nodes which are at K distance from the the given node.
# Input format :

# Line 1 : Elements in level order form (separated by space)

# (If any node does not have left or right child, take -1 in its place)

# Line 2 : Node

# Line 3 : K

# Output format : Answer nodes in different line

# Sample Input :
# 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# 3
# 1
# Sample Output :
# 9
# 6


import queue
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def printkDistanceNodeDown(root, k): 
      
    # Base Case 
    if root is None or k< 0 : 
        return 
      
    # If we reach a k distant node, print it 
    #print(k)
    if k == 0 : 
        print(root.data)  
        return 
      
    # Recur for left and right subtee 
    printkDistanceNodeDown(root.left, k-1) 
    printkDistanceNodeDown(root.right, k-1) 
  
  
def printkDistanceNode(root, target, k): 
      
    # Base Case 1 : IF tree is empty return -1 
    if root is None: 
        return -1
    #print(root.data,target.data)
    if root.data == target.data: 
        printkDistanceNodeDown(root, k) 
        return 0 
      
    # Recur for left subtree 
    dl = printkDistanceNode(root.left, target, k) 
      
    # Check if target node was found in left subtree 
    if dl != -1: 
        if dl +1 == k : 
            print(root.data) 
     
        else: 
            printkDistanceNodeDown(root.right, k-dl-2) 
 
        return 1 + dl 
  

    dr = printkDistanceNode(root.right, target, k) 
    if dr != -1: 
        if (dr+1 == k): 
            print(root.data) 
        else: 
            printkDistanceNodeDown(root.left, k-dr-2) 
        return 1 + dr 
  
    # If target was neither present in left nor in right subtree 
    return -1

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
node_data=int(input())
node=BinaryTreeNode(node_data)
k=int(input())

printkDistanceNode(root,node,k)