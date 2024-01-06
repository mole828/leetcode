#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start
from bisect import bisect_left, bisect_right
from collections import defaultdict
from functools import cache
from typing import List

# Memory Limit Exceeded
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        length = len(profit)
        @cache
        def jobMask(job: int):
            return sum(1<<t for t in range(startTime[job],endTime[job]))
        @cache
        def dp(i: int, timeMask: int) -> int:
            thisTimeMask = jobMask(i)
            # print(i,thisTimeMask)
            if timeMask & thisTimeMask:
                return 0
            newMask = timeMask | thisTimeMask
            return max(
                [dp(j, newMask) for j in range(i+1, length)],
                default=0
            ) + profit[i]
        return max(
            dp(i, 0) for i in range(length)
        )

# Time Limit Exceeded
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        length = len(profit)
        jobs = sorted(zip(startTime,endTime,profit))
        @cache
        def dp(endAt: int, i: int) -> int:
            start, end, prof = jobs[i]
            if endAt > start:
                return 0
            return max(
                [dp(end, j) for j in range(i+1, length)],
                default=0
            ) + prof 
        return max(
            dp(0, i) for i in range(length)
        )

# Time Limit Exceeded
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        length = len(profit)
        start_index: dict[int,set[int]] = defaultdict(set)
        for i in range(length):
            start = startTime[i]
            start_index[start].add(i)
        @cache
        def dp(endAt: int) -> int:
            nexts = []
            for start in start_index:
                if start < endAt:
                    continue
                for i in start_index[start]:
                    nexts.append(i)
            return max(
                [dp(endTime[i])+profit[i] for i in nexts],
                default=0,  
            )
        return dp(0)

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        length = len(profit)
        jobs = sorted(zip(startTime, endTime, profit))
        @cache 
        def dp(i: int)->int:
            if i==length:
                return 0 
            start, end, prof = jobs[i]
            begin = bisect_left(jobs, end, lo=i, key=lambda x:x[0])
            return max(
                dp(begin)+prof,
                dp(i+1)
            ) 
        return dp(0)
# @lc code=end

print(Solution().jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))
