391 · 数飞机
Medium

Description
给出飞机的起飞和降落时间的列表，用序列 interval 表示. 请计算出天上同时最多有多少架飞机？

 输入: [(1, 10), (2, 3), (5, 8), (4, 7)]
输出: 3
解释:
第一架飞机在1时刻起飞, 10时刻降落.
第二架飞机在2时刻起飞, 3时刻降落.
第三架飞机在5时刻起飞, 8时刻降落.
第四架飞机在4时刻起飞, 7时刻降落.
在5时刻到6时刻之间, 天空中有三架飞机.

1. 澄清:


2. 易错点:
   pop function need to use heapq.heappop()
   the data need to be sorted

3. 思路
   3.1 sweep line method
        build a line with start time, value to add, end time, value to add with the input
        sort the line
        scan from the begining to the end, record the maximum count during the sweeping

   3.2 priority queue method
       sort the input array
       compare the current start time with the priority queue end time, popout the time that smaller than current start time
       record the maximum length of the pq

4.1.algorithm: sweeping line, o(nlogn) time | o(n)space
def countOfAirplanes(self, airplanes):
    airplane = []
    for x in airplanes:
        airplane.append([x.start, 1])
        airplane.append([x.end, -1])

    airplane.sort()
    count = ans = 0
    for time, state in airplane:
        count += state
        ans = max(ans, count)
    return ans

def countOfAirplanes(self, airplanes):
    import heapq
    airplanes.sort(key= lambda x:x.start)
    count = 0
    ends = []
    for x in airplanes:
        while ends and ends[0]<=x.start:
            heapq.heappop(ends)
        heapq.heappush(ends, x.end)
        count = max(count, len(ends))

    return count
