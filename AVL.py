# -*- coding: utf-8 -*-
"""
Created on Wed May  5 23:06:54 2021

@author: Bo
"""
# Python code to insert a node in AVL tree

# Generic tree node class
class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1

# AVL tree class which supports the
# Insert operation
class AVL_Tree(object):

	# Recursive function to insert key in
	# subtree rooted with node and returns
	# new root of subtree.
	def insert(self, root, key):
	
		# Step 1 - Perform normal BST
		if not root:
			return TreeNode(key)
		elif key < root.val:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		# Step 2 - Update the height of the
		# ancestor node
		root.height = 1 + max(self.getHeight(root.left),
						self.getHeight(root.right))

		# Step 3 - Get the balance factor
		balance = self.getBalance(root)

		# Step 4 - If the node is unbalanced,
		# then try out the 4 cases
		# Case 1 - Left Left
		if balance > 1 and key < root.left.val:
			return self.rightRotate(root)

		# Case 2 - Right Right
		if balance < -1 and key > root.right.val:
			return self.leftRotate(root)

		# Case 3 - Left Right
		if balance > 1 and key > root.left.val:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		# Case 4 - Right Left
		if balance < -1 and key < root.right.val:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

	def leftRotate(self, z):

		y = z.right
		T2 = y.left

		# Perform rotation
		y.left = z
		z.right = T2

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		# Return the new root
		return y

	def rightRotate(self, z):

		y = z.left
		T3 = y.right

		# Perform rotation
		y.right = z
		z.left = T3

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		# Return the new root
		return y

	def getHeight(self, root):
		if not root:
			return 0

		return root.height

	def getBalance(self, root):
		if not root:
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right)

	def preOrder(self, root):

		if not root:
			return

		print("{0} ".format(root.val), end="")
		self.preOrder(root.left)
		self.preOrder(root.right)

def levelOrder(root):
    bfs=[root]
    i=0;
    while bfs:
        temp=[];
        print('Level %d'%(i));
        arr=[node.val for node in bfs]
        print(arr)
        for node in bfs:
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right);
        bfs=temp;
        
        i+=1


# Driver program to test above function
myTree = AVL_Tree()
root = None

array=['M', 'G','P','D', 'J', 'R','H','K', 'I']
array=[14,23,7,10,33,56,80,66,70]
for char in array:
    root = myTree.insert(root, char)
    
print("Leverl order traversal of the",
	"constructed AVL tree is")
levelOrder(root)