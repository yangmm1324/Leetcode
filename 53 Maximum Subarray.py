53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

1. 澄清:
   暂时想不出来

2. 易错点：
    divide and conquer 方法 记得要recursively call left and right half
    leftmax and rightmax initialization is 0 not float('-inf')
3. 思路
   方法1： 一维dp方法, kadanes algorithm， cur = max（cur + num, num）这样确保是连续的subarray， 更新ans
   方法2： 用divide and conquer， define function for the cross， left——max， right——max， cross=left——max+right——max+nums【mid】
           get the left——half， and right——half， return max (left_half, right_half, cross)

3. algorithm:-方法1， 一维dp方法
def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        maxSum = nums[0]
        cur = nums[0]

        for num in nums[1:]:
            cur = max(cur + num, num)
            maxSum = max(maxSum, cur)

        return maxSum

https://www.youtube.com/watch?v=Eo2wQIPSwrw
3. algorithm:-方法2， 用divide and conquer, o(nlogn) time |o(n) space
def maxSubArray(self, nums: List[int]) -> int:
    def maxSub(left, right):
        if left > right: return float('-inf')

        mid = (left + right) // 2
        left_max = right_max = cur = 0
        for i in range(mid - 1, left - 1, -1):
            cur += nums[i]
            left_max = max(left_max, cur)

        cur = 0
        for i in range(mid + 1, right + 1):
            cur += nums[i]
            right_max = max(right_max, cur)
        cross = left_max + right_max + nums[mid]

        left_part = maxSub(left, mid - 1)
        right_part = maxSub(mid + 1, right)

        return max(left_part, right_part, cross)

    return maxSub(0, len(nums) - 1)
