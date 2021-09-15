47. Permutations II
Medium

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

1. 澄清:


2. 易错点:
   time complexity : loose bound n*n!- assume no overlap, which is not true
   space complexity: o(n) to build the hashtable

3. 思路

   time complexity: n*n!
   The difference of this problem with the 46 permutation is the potential duplicate of the input array,
   to avoid produce the duplicate permuation, for each step, we permu with the distinct value--with the help of hashtable
   then the question is classic backtrack problem

4.1. algorithm: recursive method, classic backtrack method, o(n*n!) time, use hashtable to have distinct value
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    import collections.Counter as Counter

    permu = []
    def backtrack(path, counter):
        if len(path) == len(nums):
            permu.append(path[:])

        for num in counter:
            if counter[num] <= 0: continue

            counter[num] -= 1
            path.append(num)

            backtrack(path, counter)
            path.pop()
            counter[num] += 1

    backtrack([], Counter(nums))
    return permu
