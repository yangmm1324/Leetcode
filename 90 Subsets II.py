90. Subsets II
Medium

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

1. 澄清:


2. 易错点:
   Don't know where is the error, but was not able to get it correct with the same thought
   time complexity:
      Permutations: N*N! (we need to take care of the position for each element)
      Combination:  N*2^N (for each element, it has 2 choice of in or not in the dataset)

   Edge cases condtion:
      step 1: Look at the any potential edge/error first
      step 2: Make special treatment or stop condition for that
      step sequence is very import, work on the main part first, then later the edges cases
      in this case, actually we don't need to have a stop condition

3. 思路

   1) backtrack method + deal with the duplicate element
      backtrack:
          instead of the typical backtrack method to record at certain condition
          record every path in the result set
          remember the stop condition, actually no need to take care of the stop condition,
      duplicate:
          sort the num first
          in the recursion, skip the element that is same as the previous one


4.1. algorithm: backtrack method, n*2^n time
def subsets(self, nums: List[int]) -> List[List[int]]:
    subs = []
    def backtrack(i, path):
        subs.append(path[:])
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j-1]: continue
            path.append(nums[j])
            backtrack(j + 1, path)
            path.pop()
    backtrack(0, [])
    return subs
