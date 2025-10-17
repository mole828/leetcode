#
# @lc app=leetcode id=3003 lang=python3
#
# [3003] Maximize the Number of Partitions After Operations
#

# @lc code=start
from functools import cache


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def dfs(i: int, mask: int, changed: bool) -> int:
            if i == n:
                return 1
            bit = 1 << (ord(s[i]) - ord('a'))
            new_mask = mask | bit
            if new_mask.bit_count() > k:
                res = dfs(i+1, bit, changed) + 1
            else:
                res = dfs(i+1, new_mask, changed)
            if changed:
                return res
            for j in range(26):
                new_mask = mask | (1<<j)
                if new_mask.bit_count() > k:
                    res = max(res, dfs(i+1, 1<<j, True) + 1)
                else:
                    res = max(res, dfs(i+1, new_mask, True))
            return res
        return dfs(0, 0, False)

            
# @lc code=end

print(Solution().maxPartitionsAfterOperations("accca", 2)) 