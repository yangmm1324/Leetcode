39. Combination Sum
Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.


1. 澄清:
   need to confirm whether the element in the candidates might be negative value
   whether the element is distinct, if not need to take special care of the duplicate numbers

2. 易错点:
   if the input array is sorted, can early stop break if current > target
   if the input array is not sorted, if encounter a bigger num >target, just continue
   time complexity (details in the end of this question):
        think about the question as a tree, the longest solution would be the target//minimum number--tree height
        and the branching factor is n number, therefore, time complexity is o(n^(target/minimum)).

3. 思路
   classic backtrack problem, defines the condition to stop the loop and condition to record the paths
   then for loop to make the choice of the next possible path

4.1 algorithm:- sorted array, in theory should be faster o(N ^ (Target/Mimimum) ) time
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    combination = []
    def backtrack(i, target, path):
        if target == 0:
            combination.append(path)
            return
        for j in range(i, len(candidates)):
            num = candidates[j]
            if num > target: continue
            backtrack(j, target - num, path+[num])
    backtrack(0, target, [])
    return combination

4.2 algorithm:- sorted array, in theory should be faster
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    combination = []
    candidates.sort()
    def backtrack(i, target, path):
        if target == 0:
            combination.append(path)
            return
        for j in range(i, len(candidates)):
            num = candidates[j]
            if num > target: break
            backtrack(j, target - num, path+[num])
    backtrack(0, target, [])
    return combination

'''###
about time complexity:
The runtime of this problem is bounded by the total number of possible combinations of "candidates", because we can only use the elements found in the list. The number of combinations of a list of size N is 2^N, you can google this.

In Combination Sum 1, you are not bounded by the number of elements in the list. You can use any element in "candidates" an unlimited number of times. This makes the runtime complexity much trickier.

If you think of all possible combinations in that problem as a tree, it has a branching factor of N (unique number of candidates). Additionally, the maximum possible height of the tree is the Target divided by the vale of the smallest Candidate i.e. the longest possible combination.

For instance Target = 6, Candidates = [2,3,6] the longest possible combination is [2, 2, 2]. All valid combinations must be length 3 or shorter.

Thus the height of the tree is limited to (T/M) and the branching factor is N. Thus the max possible nodes in the combinatorial tree is N ^ (T/M). You can google this relation between the height of a tree, branching factor and number of nodes.

Hopefully this helps! I do recommend re-reading the solution for Combination Sum 1 a few times. The visual there with the tree is quite helpful.
'''
