200. Number of Islands
Medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

1. 澄清:
   can we modify the grid value in place, if not, need to maintain the visited history

2. 易错点:
   when union, should uf.parent[root_x] = root_y
                      uf.sub_size[root_y] += uf.sub_size[root_x]
               is root_x, not x
               
   don't foreget to process the cell has been visited
3. 思路
   3.1 standard dfs method
       modify the cell value in place without using any visit memory

   3.2 use union find
       add the cell with value of '1'
       then add the 2 direction cell(up and left) if met condition, then union

4.1.algorithm: use standard dfs method, o(m*n) time | o(1) space
def numIslands(self, grid: List[List[str]]) -> int:
    count = 0
    def dfs(i, j):
        if i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0': return
        grid[i][j] = '0'
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    m, n =len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j]=='0': continue
            dfs(i, j)
            count += 1
    return count

class UnionFind:

    def __init__(self):
        self.parent = {}
        self.size = 0
        self.sub_size={}

    def add(self, x):
        if x in self.parent: return
        self.parent[x] = None
        self.sub_size[x] = 1
        self.size += 1

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x !=root_y:
            self.parent[root_x]= root_y
            self.size -= 1
            self.sub_size[y] += self.sub_size[root_x]

    def find(self, x):
        root = x
        while self.parent[root] != None:
            root = self.parent[root]

        while x != root:
            original_parent = self.parent[x]
            self.parent[x] = root
            x = original_parent
        return root

def numIslands(self, grid: List[List[str]]) -> int:
    uf = UnionFind()
    m, n =len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j]=='0': continue
            uf.add((i, j))
            for x, y in (i-1, j) ,(i, j-1):
                if x<0 or x>=m or y<0 or y>=n or grid[x][y]=='0': continue
                uf.add((x,y))
                uf.union((i, j),(x,y))
    return uf.size
