适用：
1. 滑动窗口， subarray, or substring
2. o(n) time
3. o(1) space, no extra space
4. palindrome

同向双指针模板
j = 0 or j = 1
for i in range(0, n - 1):
    while j < n and (i , j的搭配不满足条件)：
        j += 1
    if (i, j的搭配满足条件):
        处理i，j的这次搭配
