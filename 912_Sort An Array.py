912. Sort an Array  Medium

Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]

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
   bubble sort optimization的sorted 维护
   quicksort的方法
   quicksort的方法模板需要牢记

3. algorithm:
def insertionSort(nums):
    if not nums: return nums
    for i in range(1,len(nums)):
        current = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = current
    return nums

def bubbleSort(nums):
    sorted=False
    n = len(nums)
    for i in range(n):
        if sorted: break
        sorted = True
        for j in range(n-1, i, -1):
            if nums[j-1]>nums[j]:
                sorted = False
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums

def mergeSort(nums):
    if len(nums)<=1: return nums
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    mergeSort(left)
    mergeSort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    nums[k:] = left[i:] or right[j:]
    return nums

def quickSort(nums, start, end):
    def partition(left, right):
        pivot = randint(left, right)
        nums[right], nums[pivot] = nums[pivot], nums[right]
        j = left
        for i in range(left, right + 1):
            if nums[i] >= nums[right]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return j - 1

    if start >= end:
        return nums

    pivotIndex = partitionRand(nums, start, end)
    quickSort(nums, start, pivotIndex - 1)
    quickSort(nums, pivotIndex + 1, end)

def countingSort(nums):
    maxValue, minValue, n = max(nums), min(nums), len(nums)
    length = maxValue - minValue + 1
    count = [0] * length
    ans =[0] * n

    for num in nums:
        count[num-minValue] += 1

    for i in range(1, length):
        count[i] += count[i-1]

    for i in range(n-1, -1, -1):
        num = nums[i]
        pos = count[num - minValue]
        count[num-minValue] -= 1
        ans[pos - 1] = num

    return ans
