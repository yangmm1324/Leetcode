33. Search in Rotated Sorted Array
Medium

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

1. 澄清:
   duplicate?

2. 易错点:

   注意mid落在哪个sort subarray的条件

3. 思路
    rotated array 可以分成两个sorted array， sort1 ----peak----sort2
    以nums[left]为比较点，判断 mid落在哪个sorted array， 所以如果nums[left]<=nums[mid],那么mid落在第一个sortedarray，
    然后根据mid落在array的范围，以及和target的比较按照标准的search去做

3. algorithm:
def search(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) //2
        if nums[mid] == target:
            return mid
        if nums[left]<= nums[mid]:
            if nums[left]<= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <target <=nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
