# Min and max
# Send Feedback
# Given a binary tree, find and return the min and max data value of given binary tree.
# Return the output as an object of PairAns class, which is already created.
# Input format :
# Elements in level order form (separated by space)
# (If any node does not have left or right child, take -1 in its place)
# Output Format :
# Max and min (separated by space)
# Sample Input :
# 8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1
# Sample Output :
# 14 1

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

INT_MIN = -2147483648
INT_MAX = 2147483647
# Problem ID 1567, Find the minimum and maximum value
def minMax(root):
    # Given a binary tree, find and return the min and max data value of given
    # binary tree. Return maximum and minimum from this function only. Largest 
    # and smallest data possible is provided through INT_MAX and INT_MIN
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root==None:
        return INT_MIN ,INT_MAX
    leftmx,leftmn=minMax(root.left)
    rightmx,rightmn=minMax(root.right)
    return max(root.data,leftmx,rightmx),min(root.data,leftmn,rightmn)
    pass

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
maximum,minimum = minMax(root)
print(maximum,minimum)