391 · Number of Airplanes in the Sky
Medium

Description
Given an list interval, which are taking off and landing time of the flight. How many airplanes are there at most at the same time in the sky?

Example 1:
Input: [(1, 10), (2, 3), (5, 8), (4, 7)]
Output: 3
Explanation:
The first airplane takes off at 1 and lands at 10.
The second ariplane takes off at 2 and lands at 3.
The third ariplane takes off at 5 and lands at 8.
The forth ariplane takes off at 4 and lands at 7.
During 5 to 6, there are three airplanes in the sky.

1. 澄清:
  暂时没有想出


2. 易错点：
如果先将第一个放进pq，一定要用heapq.heappush（）的方式添加，不然会出错
记得pop() 的时候用heapq.heappop()的方式pop，而不是用pop（）
注意heapq 2种方法的更新和返回条件，while vs if


3. algorithm:
3个方法，sweep line， presum， heapq， 其中heapq有两种写法，注意区别
sweep line： 维护一个list，添加【起点时间，1】和【结束时间，-1】，然后进行sort， 过程中update count
presum： 维护一个hashtable， 起点时间+1，结束时间-1， sort hashtable by key， 更新presum，更新返回结果
heapq： 维护一个pq，记录结束时间， sort原数组by start，方法1，如果pq里的时间都小于当前的飞机的开始时间，就全部pop， 实时更新ans by len（pq）
        方法2, 用 if 语句，仅确认一席之位，如果有free，就pop， 最后返回len（pq）

方法1： sweep line o(nlogn) time |o(n)space
def countOfAirplanes(airplanes):
    planes = []
    for plane in airplanes:
        planes.append([plane.start, 1])
        planes.append([plane.end, -1])
    planes.sort()
    count = ans = 0

    for time, state in planes:
        count += state
        ans = max(ans, count)

    return ans

方法2： presum, o(nlogn) time | o(n)space
def countOfAirplanes(airplanes):
    planes = {}
    for plane in airplanes:
        planes[plane.start] = planes.get(plane.start, 0) + 1
        planes[plane.end] = planes.get(plane.end, 0) - 1

    count = ans = 0
    for time in sorted(planes.keys()):
        count += planes[time]
        ans = max(ans, count)

    return ans

方法3-1： heapq 方法1， maintain ans， update along the road， aggressively update the pq
def countOfAirplanes(airplanes):
    import heapq
    if not airplanes: return 0
    ans = 0
    end = []

    airplanes.sort(key= lambda x: x.start)
    for plane in airplanes:
        while end and end[0]<=plane.start:
            heapq.heappop(end)
        heapq.heappush(end, plane.end)
        ans = max(ans, len(end))

    return ans

方法3-2： heapq 方法2， only free the spot for the current plane, does not update the pq aggressively
def countOfAirplanes(airplanes):
    import heapq
    if not airplanes: return 0
    ans = 0
    end = []

    airplanes.sort(key= lambda x: x.start)
    for plane in airplanes:
        if end and end[0]<=plane.start:
            heapq.heappop(end)
        heapq.heappush(end, plane.end)

    return len(end)
