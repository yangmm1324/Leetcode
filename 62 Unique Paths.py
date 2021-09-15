
62. Unique Paths
Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Input: m = 3, n = 7
Output: 28

1. 澄清:

2. 易错点：
   注意padding和初始化的关系， 此题如果用padding的话，0th行，列均为0， 同时注意[1][1]=1
   不padding的时候，[0][0]=1, 增加path number on two condition， if i>0， if j>0
                                                                注意是if，而不是elif

3. 思路
   初始化dp[0][0] = 1
   condition: if i>0: dp[][]+=dp[][]
              if j>0: dp[][]+=dp[][]


3. algorithm:
def uniquePaths(self, m: int, n: int) -> int:
    dp=[[0]*n for _ in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i>0:
                dp[i][j] += dp[i-1][j]
            if j>0:
                dp[i][j] += dp[i][j-1]

    return dp[-1][-1]
