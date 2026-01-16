#
# @lc app=leetcode id=2975 lang=python3
#
# [2975] Maximum Square Area by Removing Fences From a Field
#

# @lc code=start
from itertools import combinations
from typing import List, Set


class Solution:
    def f(self, a: List[int], mx: int) -> Set[int]:
        a += [1, mx]
        a.sort()
        # 计算 a 中任意两个数的差，保存到哈希集合中
        return set(y - x for x, y in combinations(a, 2))

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 1_000_000_007
        h_set = self.f(hFences, m)
        v_set = self.f(vFences, n)

        ans = max(h_set & v_set, default=0)
        return ans * ans % MOD if ans else -1

# @lc code=end

