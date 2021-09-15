92 · Backpack
Medium

Description
Given n items with size A_{i} A i an integer m denotes the size of a backpack. How full you can fill this backpack?

Example 1:
array = [3,4,8,5]
backpack size = 10
Output:9
Explanation:
Load 4 and 5.

1. 澄清:
   how many times can each item be used? once- 0 1 knap
                                         unlimited- 完全背包

2. 易错点：
   二维dp注意padding，否则需要定义dp[i-1][j]
   用boolean instead of actual value + operation，速度会更快
   注意boolean的初始化，第一列j =0是True
   如果二维dp要降维，则注意第二层loop的顺序，否则维护一个temp的数组

3. 思路
   二维：
       if j<A[i]: dp[i][j]= dp[i-1][j]
       else: dp[i][j] = max(dp[i-1][j], dp[i-1][j- A[i]]+ A[i])
       如果用boolean，则需要最后一行从后往前找第一个True的数值
   一维：
       第二层loop需要从后往前loop，否则就变成了完全背包，可以不限次数使用

3. algorithm:
def backPack(self, m, A): 直接operation，耗时长
    n = len(A)
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if j< A[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j -A[i-1]] + A[i-1])

    return dp[-1][-1]

def backPack(self, m, A): 采用boolean，比方法1要快
    n = len(A)
    dp = [[False] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j]
            if j >= A[i-1]:
                dp[i][j] = dp[i-1][j] |dp[i-1][j -A[i-1]]

    for i in range(m, -1, -1):
        if dp[-1][i]:
            return i

 def backPack(self, m, A): 降维1一维
     n = len(A)
     dp = [0]*(m+1)

     for i in range(n):
         for j in range(m, A[i]-1, -1):
             dp[j] = max(dp[j], dp[j- A[i]]+ A[i])

    return dp[-1]
