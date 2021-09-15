144. Binary Tree Preorder Traversal
Easy

Given the root of a binary tree, return the inorder traversal of its nodes' values.Example 1:
Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]

1. 澄清:


2. 易错点:


3. 思路
    preorder -- process the current node
                find left node till
                go to right

3. algorithm:- recursive method, o(n) time |o(n) space
def preorderTraversal(self, root: TreeNode) -> List[int]:

    def helper(root, ans):
        if not root: return
        ans.append(root.val)
        helper(root.left, ans)
        helper(root.right, ans)
        return ans

    return helper(root,[])

algorithm:- iterative method, o(n) time |o(n) space
def preorderTraversal(self, root: TreeNode) -> List[int]:
    stack = []
    ans = []
    while root or stack:
        while root:
            ans.append(root.val)
            stack.append(root)
            root = root.left
        root = stack.pop()
        root = root.right

    return ans
