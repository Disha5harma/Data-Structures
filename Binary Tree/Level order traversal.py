# Level order traversal
# Send Feedback
# Given a binary tree, print the level order traversal. Make sure each level start in new line.
# Input format :

# Elements in level order form (separated by space). If any node does not have left or right child, take -1 in its place.

# Output Format :

# Elements are printed level wise, each level in new line (separated by space).

# Sample Input :
# 5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1
# Sample Output :
# 5 
# 6 10 
# 2 3 
# 9


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    main_queue=queue.Queue()
    aux_queue=queue.Queue()
    main_queue.put(root)
    while(not main_queue.empty()):
        while(not main_queue.empty()):
            curr=main_queue.get()
            print(curr.data,end=' ')
            if(curr.left is not None):
                aux_queue.put(curr.left)
            if(curr.right is not None):
                aux_queue.put(curr.right)
        print()
        main_queue,aux_queue=aux_queue,main_queue

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
#n=int(input())
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
printLevelATNewLine(root)