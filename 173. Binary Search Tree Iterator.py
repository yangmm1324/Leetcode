173. Binary Search Tree Iterator
Medium

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]


1. 澄清:
   The root does not change, that means we build the array once, and each function call only have o(1) time

2. 易错点:


3. 思路
   method 1: just use the inorder traveral, get the array data and maintain the index of the callingm, bit slower o(n) build, o(1) call next
   method 2: use the iterative inorer traversal concept, distribute the entire traversal by number of calls of next function, o(h) time worst

4.1 algorithm:- traversal the BST tree into an array, and maintain the index, useful when the root does not change
class BSTIterator:

    def __init__(self, root: TreeNode):
        stack = []
        self.bst = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.bst.append(root.val)
            root = root.right
        self.index = 0
    def next(self) -> int:
        self.index += 1
        return self.bst[self.index - 1]

    def hasNext(self) -> bool:
        return self.index < len(self.bst)

4.2 algorithm:- distribute the traversal into the number of function calls-Next(), worst case o(h)
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.root = root
    def next(self) -> int:
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
        root = self.stack.pop()
        self.root = root.right
        return root.val

    def hasNext(self) -> bool:
        return self.index < len(self.bst)
