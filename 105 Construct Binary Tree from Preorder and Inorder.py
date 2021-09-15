105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and
inorder is the inorder traversal of the same tree, construct and return the binary tree.
Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

1. 澄清:


2. 易错点:


3. 思路
    preorder--root, left, right
    inorder --left, root, right
    therefore the index of root, split the inorder into left and right part to the current node
              preorder left count = index of root - inorder left boundary
              therefore:
                  for left side: preorder range: preorder_left + 1, preorder_left + index - inorder_left
                                 inorder range:  inorder_left, index - 1
                  for right side: preorder range: preorder_left + index - inorder_left + 1, preorder_right
                                 inorder range: index + 1, inorder_right

3. algorithm:- recursive method, Avg(nlogn), worst case(n^2)
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not inorder: return None

        val = preorder.pop(0)
        index = inorder.index(val)
        root = TreeNode(val)

        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index+1:])

        return root
o(n) time | o(n) space
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

    if not preorder: return None
    index = {}
    for i, num in enumerate(inorder):
        index[num] = i

    def helper(pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right: return None

        val = preorder[pre_left]
        root = TreeNode(val)
        pos = index[val]

        root.left = helper(pre_left+1, pre_left+pos- in_left, in_left, pos-1)
        root.right= helper(pre_left+pos-in_left+1, pre_right, pos+1, in_right)

        return root

    return helper(0, len(preorder)-1, 0, len(inorder)-1)
