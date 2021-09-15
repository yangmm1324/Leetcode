145. Binary Tree Postorder Traversal
Easy

Given the root of a binary tree, return the postorder traversal of its nodes' values.
Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]

1. 澄清:


2. 易错点:
   It is not as easy as the iterative method for the inorder and preorder traversal

   when we check the right of the stack[-1],
                be cautious that if there is no right, we did not assign the root value, we track back the chain and record
                the chain value, leave root unassigned, that means, we use another variable for checking the iteration

3. 思路
    postorder: still use stack
               check the root first, if there is still root, traverse to the left
               else check the last pushed node.right,
                   if the last pushed node has no right,
                             then add the node,val to the result,
                             then iteratively checked the current node is the right of the last node in stack--which suggests the right side has all being visited.
                             add the node.val to the result.
                   else: start the root from the node.right


3. algorithm:- recursive method,
def postorderTraversal(self, root: TreeNode) -> List[int]:

    def helper(root, ans):
        if not root: return
        helper(root.left, ans)
        helper(root.right, ans)
        ans.append(root.val)
        return ans

    return helper(root,[])

algorithm:- iterative method, o(n) time |o(h) space except the ans space, this algorithm is also often used to find the maximum height of a binary tree- max( len(stack))
https://www.youtube.com/watch?v=xLQKdq0Ffjg
def postorderTraversal(self, root: TreeNode) -> List[int]:
    stack = []
    ans = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            right = stack[-1].right
            if right is None:
                cur = stack.pop()
                ans.append(cur.val)
                while stack and cur == stack[-1].right:
                    cur = stack.pop()
                    ans.append(cur.val)
            else:
                root = right
    return ans
