# BST Class

# Implement the BST class which includes following functions -
# 1. search
# Given an element, find if that is present in BSt or not. Return true or false.
# 2. insert -
# Given an element, insert that element in the BST at the correct position. Assume unique elements will be given.
# 3. delete -
# Given an element, remove that element from the BST. If the element which is to be deleted has both children, replace that with the minimum element from right sub-tree.
# 4. printTree (recursive) -
# Print the BST in ithe following format -
# For printing a node with data N, you need to follow the exact format -
# N:L:x,R:y
# wherer, N is data of any node present in the binary tree. x and y are the values of left and right child of node N. Print the children only if it is not null.
# There is no space in between.
# You need to print all nodes in the recursive format in different lines.
# Note : main function is given for your reference which we are using internally to test the class.


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self, root):
        if root == None:
            return
        print(root.data, end = ":")
        if root.left != None:
            print("L:",end='')
            print(root.left.data,end=',')
        if root.right != None:
            print("R:",end='')
            print(root.right.data,end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    
    def printTree(self):
        self.printTreeHelper(self.root)
    
    
    def search(self, data):
    #Implement this function here
        return self.searchhelper(self.root,data)
    
    def searchhelper(self,root,data):
        if root==None:
            return False
        if root.data==data:
            return True
        if root.data>data:
            return self.searchhelper(root.left,data)
        else:
            return self.searchhelper(root.right,data)
        
    def insert(self, data):
    #Implement this function here
        self.numNodes+=1
        self.root=self.inserthelper(self.root,data)
        
    def min(self,root):
        if root==None:
            return 10000
        
        if root.left==None:
            return root.data
        
        return self.min(root.left)
    
    def inserthelper(self,root,data):
        if root==None:
            curr=BinaryTreeNode(data)
            root=curr
            return root 
        if root.data>data:
            root.left=self.inserthelper(root.left,data)
            return root
        else:
            root.right=self.inserthelper(root.right,data)
            return root
    
    def delete(self,data):
    #Implement this function here
        deleted,newroot=self.deletehelper(self.root,data)
        if deleted:
            self.numNodes-=1
        self.root=newroot
        return deleted 
        
    def deletehelper(self,root,data):

        if root==None:
            return False,None

        if root.data>data:
            deleted,newleft=self.deletehelper(root.left,data)
            root.left=newleft
            return True,root
        
        if root.data<data:
            deleted,newright=self.deletehelper(root.right,data)
            root.right=newright
            return True,root
        
        if root.left==None and root.right==None:
            return True,None
        
        if root.left==None:
            return True,root.right
        
        if root.right==None:
            return True,root.left
    
        replacement=self.min(root.right)
        root.data=replacement
        deleted,newright=self.deletehelper(root.right,replacement)
        root.right=newright
        return True,root
    
    def count(self):
        return self.numNodes
b = BST()
li = [int(ele) for ele in input().split()]
i = 0
while(i < (len(li) )):
    choice = li[i]
    
    if choice == 1:
        data = li[i+1]
        b.insert(data)
        i+=2
    elif choice == 2:
        data = li[i+1]
        b.delete(data)
        i+=2
    elif choice == 3:
        data = li[i+1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
        i+=2
    else:
        b.printTree()
        i+=1