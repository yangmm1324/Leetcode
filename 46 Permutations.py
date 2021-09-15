46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

1. 澄清:
   is there any duplicate in the input array

2. 易错点:
   time complexity
   注意 recursive 和 iterative index的区别， recursive因为每个pos都会取到，所以不需要到length
        iterative 需要往前sub里插入当前的值，需要考虑到sub的最后一个pos，所以需要到sub的整个长度

   since we are inserting the num into different position, the entire array should also be included, the index range should include the last indx



3. 思路

   time complexity: n*n!
   1) Recursive method
      very similar template to the backtrack method
      if there is no element left, then append the path to the result
      for any position of the array,
            put the element at the end of the current path, and continue with the left elements

   2) Iterative method
      maintain a current array set with small n element permuation so far
      for element in the array:
          for subset in resultset so far, insert the element to every position of the subset

4.1. algorithm: recursive method, classic backtrack method, o(n*n!) time
def permute(self, nums: List[int]) -> List[List[int]]:
    paths = []
    def backtrack(arr, path):
        if not arr:
            paths.append(path)

        for i in range(len(arr)):
            backtrack(arr[:i]+arr[i+1:], path+[arr[i]])

    backtrack(nums, [])
    return paths

4.2 algorithm: iterative method, o(n*n!) time

def permute(self, nums: List[int]) -> List[List[int]]:
    permu = [[]]

    def insert(permu, num):
        ans = []
        for sub in permu:
            for i in range(len(sub)+1):
                ans.append(sub[:i]+[num]+sub[i:])
        return ans

    for num in nums:
        permu = insert(permu, num)

    return permu
