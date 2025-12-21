#
# @lc app=leetcode id=955 lang=python3
#
# [955] Delete Columns to Make Sorted II
#

# @lc code=start
import enum
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        a = [''] * n
        ans = 0
        for j in range(m):
            for i in range(n - 1):
                if a[i] + strs[i][j] > a[i + 1] + strs[i + 1][j]:
                    ans += 1
                    break
            else:
                for i, s in enumerate(strs):
                    a[i] += s[j]
        return ans

# @lc code=end

