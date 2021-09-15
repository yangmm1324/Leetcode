
75. Sort Colors Medium
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

1. 澄清:
  null array
  required stable sort or not?
     Yes: bublle_sort, insertion_sort,Mergesort;
     No: Quicksort, heapsort
  time complexity?
    o(n^2): bubble_sort, insertion_sort-o(n2)
    o(nlogn): mergeSort, quicksort, heapsort
    o(n): counting sort, if maximum value is close to n
  what is the range of the element, num[i]<0, need to be careful with counting sort

  optimization:
      if the nums is almost sort, we can use insertion or bublle sort
2. 易错点：
   counting sort, remember to deal with the negative value, index - minValue
   when use 3 area: zero, one, two, be careful of the current pointer advance condition,
                    when swap with the pointer for two, we should not advance the current index 

3. 思路
   分成3个区间，0-zero_index, cur, two_index-n, check current value, and swap value with zero_index, two_index

3. algorithm:
def countingSort(nums):
    maxValue, minValue, n = max(nums), min(nums), len(nums)
    length = maxValue - minValue + 1
    count = [0] * length
    temp =[0] * n

    for num in nums:
        count[num-minValue] += 1

    for i in range(1, length):
        count[i] += count[i-1]

    for i in range(n-1, -1, -1):
        temp[count[nums[i] - minValue] - 1] = nums[i]
        count[nums[i]-minValue] -= 1
    for i in range(n):
        nums[i] = temp[i]

follow up - one pass, o(n)time, o(1)space

def countingSort(nums):
    zero = cur = 0
    two = len(nums) - 1
    while cur <= two:
        if nums[cur] == 0:
            nums[zero], nums[cur] = nums[cur], nums[zero]
            zero += 1
            cur += 1
        elif nums[cur] == 2:
            nums[cur], nums[two] = nums[two], nums[cur]
            two -= 1
        else:
            cur += 1
