#
# @lc app=leetcode id=2138 lang=python3
#
# [2138] Divide a String Into Groups of Size k
#

# @lc code=start
from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        res = []
        for i in range(0, n, k):
            res.append(s[i:i+k])
        if len(res[-1]) != k:
            res[-1] += fill * (k - len(res[-1]))
        return res
        
# @lc code=end

