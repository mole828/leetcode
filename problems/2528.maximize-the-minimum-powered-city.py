#
# @lc app=leetcode id=2528 lang=python3
#
# [2528] Maximize the Minimum Powered City
#

# @lc code=start
from itertools import accumulate
from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        s = list(accumulate(stations, initial=0))
        power = [s[min(n, i+r+1)] - s[max(0, i-r)] for i in range(n)]
        def check(low: int) -> bool:
            diff = [0] * n
            sum_d = built = 0
            for i, p in enumerate(power):
                sum_d += diff[i]
                m = low - (p+sum_d)
                if m <= 0:
                    continue
                built += m
                if built > k:
                    return False
                sum_d += m
                if (right:=i+r*2+1) < n:
                    diff[right] -= m
            return True
        
        mn = min(power)
        left, right = mn, mn + k + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left

# @lc code=end


print(Solution().maxPower([1,2,4,5,0], 1, 2))  # 5
print(Solution().maxPower([4,4,4,4], 0, 0))  # 4