#
# @lc app=leetcode id=539 lang=python3
# @lcpr version=
#
# [539] Minimum Time Difference
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import bisect
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def to_minutes(timePoint):
            a,b = timePoint.split(":")
            return int(a) * 60 + int(b)
        times = [to_minutes(timePoint) for timePoint in timePoints]
        full_day = 24 * 60
        full_times = []
        for time in times:
            full_times.insert(bisect.bisect_left(full_times, time), time)
            full_times.insert(bisect.bisect_left(full_times, time + full_day), time + full_day)
        # print(full_times)
        return min([full_times[i + 1] - full_times[i] for i in range(len(full_times) - 1)])
# @lc code=end



#
# @lcpr case=start
# ["23:59","00:00"]\n
# @lcpr case=end

# @lcpr case=start
# ["00:00","23:59","00:00"]\n
# @lcpr case=end

#

