#
# @lc app=leetcode id=1482 lang=python3
# @lcpr version=
#
# [1482] Minimum Number of Days to Make m Bouquets
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from bisect import bisect_left
from functools import cache
from typing import Callable, List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = m * k
        if len(bloomDay) < n:
            return -1
        @cache
        def day_pass(d: int):
            print(f"day_pass({d})")
            mm = 0
            kk = k
            for day in bloomDay:
                if day <= d:
                    kk -= 1
                else:
                    kk = k
                if not kk:
                    mm += 1
                    kk = k
            return mm
        class FuncArray:
            def __init__(self, f: Callable[[int], int]) -> None:
                self.f = f
            def __getitem__(self, index: int) -> int:
                return self.f(index)
        func_array = FuncArray(day_pass)
        day = bisect_left(func_array, m, lo=min(bloomDay), hi=max(bloomDay))
        print({"day": day})
        return day
# @lc code=end

print(Solution().minDays([7,7,7,7,12,7,7], 2, 3))
print(Solution().minDays([10,10], 1, 1))

#
# @lcpr case=start
# [1,10,3,10,2]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,10,3,10,2]\n3\n2\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,12,7,7]\n2\n3\n
# @lcpr case=end

#

