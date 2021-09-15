297. Serialize and Deserialize Binary Tree
Hard

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Example 1:

Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]


1. 澄清:


2. 易错点:
   不是complete binary tree， deserize的时候不可以用2*i+1， 2*i+ 2


3. 思路
    preorder tranverse to serialize, 需要谨慎的是当root是None的时候，return的值 是‘null，’
            然后采用deque的方法，如果当前的值为null，则pop（0），return None 否则生成root，pop（0），然后左右支
            不能特别掌握这个方法

    bfs level by level method: 会保留2*‘#’ for a leaf node， 形成serialization string
           deserialize的时候，维护一个index 和 node的清单，loop node的list，如果当前值不是‘#’ 就先assign node。left值，并且将node。left加进node的清单，不管是否是‘#’则将index+1，
           然后同样的进行node.right的节点更新,同样如果有node。right增加进node的清单，并且不管有没有right节点都累计index

3. algorithm:- preorder method
def serialize(self, root):
    def helper(root, arr):
        if not root:
            arr.append('Null,')
            return arr
        arr.append(str(root.val) + ',')
        helper(root.left, arr)
        helper(root.right, arr)
        return arr
    arr = helper(root, [])
    return ''.join(arr)

def deserialize(self, data):
    data = data.split(',')
    data = collections.deque(data)

    def helper(data):
        if data[0] == 'Null':
            data.popleft()
            return None
        root = TreeNode(int(data[0]))
        data.popleft()
        root.left = helper(data)
        root.right= helper(data)
        return root
    return helper(data)

3. algorithm:- bfs level by level method
def serialize(self, root):
    if not root: return ''
    arr = []
    bfs = [root]
    for node in bfs:
        if node:
            bfs.append(node.left)
            bfs.append(node.right)
        arr.append('#' if not node else str(node.val))
    return ','.join(arr)

def deserialize(self, data):
    if not data: return None
    data = data.split(',')
    root = TreeNode(int(data[0]))
    index = 1
    bfs = [root]
    for node in bfs:
        if data[index] != '#':
            node.left = TreeNode(int(data[index]))
            bfs.append(node.left)
        index += 1
        if data[index] != '#':
            node.right = TreeNode(int(data[index]))
            bfs.append(node.right)
        index += 1

    return root
