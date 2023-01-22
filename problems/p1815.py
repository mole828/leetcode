from functools import cache
from typing import List, Tuple

# link：https://leetcode.cn/problems/maximum-number-of-groups-getting-fresh-donuts/solution/by-endlesscheng-r5ve/

class Solution:
    def maxHappyGroups(self, m: int, groups: List[int]) -> int:
        cnt = [0] * m
        for x in groups:
            cnt[x % m] += 1

        @cache  # 记忆化
        def dfs(left: int, cnt: Tuple[int]) -> int:
            res = 0
            cnt = list(cnt)
            for x, c in enumerate(cnt):  # 枚举顾客
                if c:  # cnt[x] > 0
                    cnt[x] -= 1
                    res = max(res, (left == 0) + dfs((left + x + 1) % m, tuple(cnt)))  # x 从 0 开始，这里要 +1
                    cnt[x] += 1
            return res
        return cnt[0] + dfs(0, tuple(cnt[1:]))  # 转成 tuple 这样能记忆化
