#
# @lc app=leetcode id=664 lang=python3
# @lcpr version=
#
# [664] Strange Printer
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache

import numpy as np


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(start, end):
            if start == end:
                return 1
            res = np.inf
            if s[start] == s[end]:
                res = dfs(start, end - 1)
            else:
                for i in range(start, end):
                    res = min(res, dfs(start, i) + dfs(i + 1, end))
            return res
        return dfs(0, n - 1)
# @lc code=end



#
# @lcpr case=start
# "aaabbb"\n
# @lcpr case=end

# @lcpr case=start
# "aba"\n
# @lcpr case=end

#

