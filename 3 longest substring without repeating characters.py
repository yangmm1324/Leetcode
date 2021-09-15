3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

1. 澄清:
   暂时想不出来

2. 易错点：
   更新left pointer的时候注意需要和当前left 和 index【char】+1 之间取较大值
   不确定用hashtable的方法是o（1）还是o(n)space

3. 思路
   使用two pointers的方式，如果char之前出现，则更新left 至left和char 之前index+1 之间的最大值，并更新maxLen

3. algorithm:-方法1 用hashtable的方法，同样是two pointer o（n）time
def lengthOfLongestSubstring(self, s: str) -> int:
    index = {}
    maxLen = 0
    left = 0
    for right, char in enumerate(s):
        if char in index:
            left = max(left, index[char] + 1)
        maxLen = max(maxLen, right - left + 1)
        index[char] = right

    return maxLen

3. algorithm:-方法2 用hashtable的方法，同样是two pointer o（n）time， o（1）space
def lengthOfLongestSubstring(self, s: str) -> int:
    maxLen = 0
    index = [-1] * 256
    left = 0

    for right, char in enumerate(s):

        char = ord(char)
        if index[char] != -1 and index[char] + 1 > left:
            left = index[char] + 1

        maxLen = max(maxLen, right - left + 1)
        index[char] = right

    return maxLen
