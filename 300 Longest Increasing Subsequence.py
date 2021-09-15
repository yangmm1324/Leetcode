300. Longest Increasing Subsequence
Medium

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some
or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

1. 澄清:
   edges cases

2. 易错点:
   dp method, time sequence, depends on more than 1 pos before current pos,
           note here, we cannot update the current value to the maximum so far, as we need to use current pos to
           calculate next pos

           also pay attention to the initialization of each pos value

   greedy + binary search,
            note here, we need to find the left pos that are smaller or equal than current element, use bisect_left
            if we use bisect, or bisect_right, then the answer will generate non decreasing array
3. 思路
   3.1 use dp method
   time sequence, current state depends on more than 1 state, loop every element before current pos,
   note

4.1.algorithm: use dp method, two loops, sequences II, depends on every pos before current pos, o(n^2) time|o(n)space
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[1]*n

        for i in range(n):
            for j in range(i):
                if nums[i]<=nums[j]: continue
                dp[i] = max(dp[i], dp[j]+1)

        return max(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        for n in nums:
            index = bisect.bisect_left(arr, n)
            if index == len(arr):
                arr.append(n)
            else:
                arr[index] = min(arr[index], n)

        return len(arr)
