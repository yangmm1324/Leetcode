1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

1. 澄清:
   暂时想不出来

2. 易错点：


3. 思路
   记录之前出现过的数字的index，如果target-num的数字层出现过，返回两个index

3. algorithm:
def twoSum(self, nums: List[int], target: int) -> List[int]:
    index = {}

    for i, num in enumerate(nums):
        if target - num in index:
            return [index[target - num], i]
        index[num] = i
