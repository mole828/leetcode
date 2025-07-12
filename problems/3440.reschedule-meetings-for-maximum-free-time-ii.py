#
# @lc app=leetcode id=3440 lang=python3
#
# [3440] Reschedule Meetings for Maximum Free Time II
#

# @lc code=start
from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        free = [startTime[0]] + [s - e for s, e in zip(startTime[1:], endTime)] + [eventTime - endTime[-1]]

        a = b = c = -1
        for i, sz in enumerate(free):
            if a < 0 or sz > free[a]:
                a, b, c = i, a, b
            elif b < 0 or sz > free[b]:
                b, c = i, b
            elif c < 0 or sz > free[c]:
                c = i

        ans = 0
        for i, (s, e) in enumerate(zip(startTime, endTime)):
            sz = e - s
            if i != a and i + 1 != a and sz <= free[a] or \
               i != b and i + 1 != b and sz <= free[b] or \
               sz <= free[c]:
                ans = max(ans, free[i] + sz + free[i + 1])
            else:
                ans = max(ans, free[i] + free[i + 1])
        return ans

# @lc code=end

print(Solution().maxFreeTime(eventTime = 10, startTime = [0,3,7,9], endTime = [1,4,8,10]))