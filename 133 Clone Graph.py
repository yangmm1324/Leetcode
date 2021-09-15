133. Clone Graph
Medium

Description
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Example 1:
Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed).
For example, the first node with val == 1, the second node with val == 2, and so on.
The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1.
You must return the copy of the given node as a reference to the cloned graph.

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

1. 澄清:
   is there any circle in the graph

2. 易错点:
   if there is circle in the graph, we need to remember the visited node,
   otherwise will be endless loop

3. 思路
    -- to simplify, dfs+memorization--to deal with the circle
        similar as dfs to tree traversal, the difference is circle
        as there is circle, need to remember previous constructed node,
        Construct the root and fill the root.neighbors recursively
    -- time complexity, typically graph problem has time complexity of o(V+E)

4.1. algorithm:  O(V+E) time
def cloneGraph(self, node: 'Node') -> 'Node':
    if not node: return None
    clone = {}

    def helper(node):
        if node in clone: return clone[node]
        if not node: return None

        node_copy = Node(node.val)
        clone[node] = node_copy

        for nei in node.neihbors:
            node_copy.neighbors.append(helper(nei))

        return node_copy
    return helper(node)
