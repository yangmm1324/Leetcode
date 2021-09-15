78. Subsets
Medium

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

1. 澄清:
   is there any duplicate in the input array

2. 易错点:
   time complexity:
      Permutations: N*N! (we need to take care of the position for each element)
      Combination:  N*2^N (for each element, it has 2 choice of in or not in the dataset)

   Edge cases condtion:
      step 1: Look at the any potential edge/error first
      step 2: Make special treatment or stop condition for that
      step sequence is very import, work on the main part first, then later the edges cases
      in this case, actually we don't need to have a stop condition

3. 思路

   1) bfs concept
      current layer have all the combination till the nth element so far
      cumulative the result with the current set combination with the current element
   2) backtrack method
      instead of the typical backtrack method to record at certain condition
      record every path in the result set
      remember the stop condition, actually no need to take care of the stop condition,


4.1. algorithm: iterative bfs concept method, n*2^n time
def subsets(self, nums: List[int]) -> List[List[int]]:
    subs = [[]]

    for num in nums:
        subs += [sub +[num] for sub in subs]
    return subs

4.1. algorithm: backtrack method, n*2^n time
def subsets(self, nums: List[int]) -> List[List[int]]:
    subs = []
    def backtrack(i, path):
        subs.append(path[:])
        for j in range(i, len(nums)):
            path.append(nums[j])
            backtrack(j + 1, path)
            path.pop()
    backtrack(0, [])
    return subs
