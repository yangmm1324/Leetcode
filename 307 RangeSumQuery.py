307. Range Sum Query - Mutable
Medium

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between
indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8

1. 澄清:
   range inclusivity

2. 易错点:



3. 思路
   3.1 use segment tree
   segment tree can return the min,max, sum for a given range in log(n) time,
                has a structure of tree represented in array as priority queue
                left child 2*i, right chile 2*i +1
                parent (i-1)//2
   when sum the range, then we only add the parent

4.1.algorithm:
class SegementTree:
    def __init__(self):
        self.size = len(nums)
        self.tree = [0]*self.size + nums
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i <<1 |1]
    def update(self, i, val):
        n = self.size + i
        self.tree[n] = val
        while n > 1:
            self.tree[n >> 1] = self.tree[n] + self.tree[n ^ 1]
            n >>= 1

    def sumRange(self, left, right):
        left += self.size
        right += self.size
        res = 0

        while left < right:
            if left & 1:
                res += self.tree[left]
                left += 1
            if right & 1 == 0:
                res += self.tree[right]
                right -= 1 
            left >>= 1
            right >>= 1

        return res
