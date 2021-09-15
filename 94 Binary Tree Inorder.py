94. Binary Tree Inorder Traversal
Easy

Given the root of a binary tree, return the inorder traversal of its nodes' values.Example 1:
Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

1. 澄清:


2. 易错点:
   o(n) time |o(1) space
   morris traversal,
          if there is left side:
              find the rightmost predessor of the left child
              if the rightmost predessor does not connect to the current root:
                 set the connection and move the current node to node left child
              else
                 remove the connection to the root-- means we have traverse all the nodes from the left
                 record the current node ## this step is very important
                 move the current node to the right side
          else
             record the current node -- have no left child, so just record the current node and move the current node right
             move the current node to the right side

3. 思路
    inorder -- find left until leaf, then get the current node value, then go to right

3. algorithm:- recursive method, o(n) time |o(n) space
def inorderTraversal(self, root: TreeNode) -> List[int]:

    def helper(root, ans):
        if not root: return
        helper(root.left, ans)
        ans.append(root.val)
        helper(root.right, ans)
        return ans

    return helper(root,[])

algorithm:- iterative method, o(n) time |o(n) space
def inorderTraversal(self, root: TreeNode) -> List[int]:
    stack = []
    ans = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        ans.append(root.val)
        root = root.right

    return ans

def morrisInorder(self, root):
    ans = []
    while root:
        if root.left:
            cur = root.left
            while cur.right and cur.right != root:
                cur = cur.right
            if cur.right is None:
                cur.right = root
                root = root.left
            else:
                ans.append(root.val)
                cur.right = None
                root = root.right
        else:
            ans.append(root.val)
            root = root.right
    return ans
