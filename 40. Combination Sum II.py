40. Combination Sum II
Medium

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

1. 澄清:
   whether there is negative value in the input array

2. 易错点:
   1. method 1 - update path and pop()---use the path as pointer to the array---time complexity is smaller?
      if ....:
          paths.append(path[:])
      path += [num]
      dfs (...,path)
      path.pop()

      when we copy to the result, we should have  a deep copy,
   2. method 2 - copy the path to the function -- time complexity is larger?
      when we add the path to the result, don't need to have a deep copy
      if ....:
          paths.append(path)
      dfs (..., path+[num])

   not sure about the time complexity

3. 思路
   similar as the combination sum 39, the difference is to only use the num once, and no duplicate combinations
   this means, during the iteration, we can not use the same current index, also for the next same number, we should skip the expliration
   as the previous same num has done all the exploration.
   we can use two methods to avoid the duplicate exploration,
      1. use hashing method to record the frequence of the nums, personally don't think it
         is any necessary the complexity, as the overall time complexity is way higher than the sorting.
      2. the other easier method is to sort the input array.


4.1. algorithm: use the sort method, and copy array in the function call, (2**n)time ??
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    combination = []
    candidates.sort()

    def backtrack(i, target, path):
        if target == 0:
            combination.append(path)

        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j-1]: continue
            num = candidates[j]

            if num > target: break
            backtrack(j+1, target - num, path+[num])

    backtrack(0, target, [])
    return combination

4.2 algorithm: use the sort method, and manipulate with the array, (2**n)time ??
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    combination = []
    candidates.sort()

    def backtrack(i, target, path):
        if target == 0:
            combination.append(path[:])

        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j-1]: continue
            num = candidates[j]

            if num > target: break
            path += [num]
            backtrack(j+1, target - num, path)
            path.pop()

    backtrack(0, target, [])
    return combination
