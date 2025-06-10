#
# @lc app=leetcode id=3442 lang=python3
#
# [3442] Maximum Difference Between Even and Odd Frequency I
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maxDifference(self, s: str) -> int:
        counter: dict[str, int] = defaultdict(int)
        for c in s:
            counter[c] += 1
        odd_values: list[int] = []
        even_values: list[int] = []
        for v in counter.values():
            if v % 2 == 0:
                even_values.append(v)
            else:
                odd_values.append(v)

        max_odd = max(odd_values)
        min_even = min(even_values)
        return max_odd - min_even

# @lc code=end

