63. Unique Paths II
Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and space is marked as 1 and 0 respectively in the grid.

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

1. 澄清:


2. 易错点：


3. 思路
   early return if start and end point is obstacle
   two for loop, if current cell is obstacle: continue
                 if i>0:  [][]+=[i-1][j]
                 if j>0:  [][]+=[i][j-1]

3. algorithm:
def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    if not obstacleGrid: return 0
    if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: return 0

    m, n = len(obstacleGrid), len(obstacleGrid[0])

    dp = [[0]*n for _ in range(m)]
    dp[0][0]= 1

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:  continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]

    return dp[-1][-1]
