# Construct BST
# Send Feedback
# Given a sorted integer array A of size n which contains all unique elements. You need to construct a balanced BST from this input array. Return the root of constructed BST.
# Note : If array size is even, take first mid as root.
# Input format :
# Line 1 : Integer n (Size of array)
# Line 2 : Array elements (separated by space)
# Output Format :
# BST elements (in pre order traversal, separated by space)
# Sample Input :
# 7
# 1 2 3 4 5 6 7
# Sample Output :
# 4 2 1 3 6 5 7 


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    # Given a sorted integer array A of size n which contains all unique
    # elements. You need to construct a balanced BST from this input array.
    # Return the root of constructed BST. If array size is even, take first mid
    # as root.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if not(lst):
        return 
    if len(lst)% 2==0:
        ri=(len(lst)//2)-1
    else:
        ri=(len(lst)//2)
    root=BinaryTreeNode(lst[ri])
    left=lst[:ri]
    
    right=lst[ri+1:]
    root.left=constructBST(left)
    root.right=constructBST(right)
    return root
    pass

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
root=constructBST(lst)
preOrder(root)