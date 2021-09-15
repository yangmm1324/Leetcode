77. Combinations
Medium

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

1. 澄清:


2. 易错点:
   not sure about time complexity

3. 思路

   classic backtrack question, early stop if k is larger than the rest element


4.1. algorithm: my guess of the time complexity is 2^n
def combine(self, n, k):
    comb = []
    def backtrack(m, k, path):
        if k > n - m + 1: return
        if k == 0:
            comb.append(path[:])
        for i in range(m, n+1):
            backtrack(i + 1, k - 1, path+[i])

    backtrack(1, k, [])
    return comb
