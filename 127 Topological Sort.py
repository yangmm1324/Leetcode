127 · 拓扑排序
Medium

Description
给定一个有向图，图节点的拓扑排序定义如下:

对于图中的每一条有向边 A -> B , 在拓扑排序中A一定在B之前.
拓扑排序中的第一个节点可以是图中的任何一个没有其他节点指向它的节点.
针对给定的有向图找到任意一种拓扑排序的顺序.

Example 1:
Input: graph = {0,1,2,3#1,4#2,4,5#3,4,5#4#5}

输出：
[0, 1, 2, 3, 4, 5]

1. 澄清:
   the type of returned value

2. 易错点:


3. 思路
     can use both bfs and dfs, however dfs is not recommended to use during interview
   time complexity:
    假设n个点，m条边；
    记录拓扑序空间复杂度为O(n)，记录入度最坏复杂度为O(n)，空间复杂度O(n)；
    记录每个点的入度为O(m)，拓扑排序为O(m)，时间复杂度O(m)。

    first build the indegree of the vertex,
    start with the vertext has no prerequiste
    use deque to pop the early entered vertex
    for each vertex, check the neighbors,
        decrease the neighbor indegree
        if the neighbor vertex has no other edges
            the vertex is ready to put into the queue

4.1. algorithm: use bfs method
def topSort(self, graph):
    def buildIndegree(graph):
        indegree = { x:0 for x in graph}
        for node in graph:
            for nei in node.neighbors:
                indegree[nei] += 1
        return indegree

    indegree = buildIndegree(graph)
    start = [x for x in indegree if indegree[x] == 0]
    queue = collections.deque(start)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in node.neighbors:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    return order

def topSort(self, graph): # dfs method
        indegree = {x: 0 for x in graph}
        for i in graph:
            for j in i.neighbors:
                indegree[j] += 1

        ans = []
        for i in graph:
            if indegree[i] == 0:
                self.dfs(i, indegree, ans)
        return ans

    def dfs(self, i, indegree, ans):
        ans.append(i)
        indegree[i] -= 1
        for j in i.neighbors:
            indegree[j] -= 1
            if indegree[j] == 0:
                self.dfs(j, indegree, ans)
