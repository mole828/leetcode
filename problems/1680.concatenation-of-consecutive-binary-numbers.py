#
# @lc app=leetcode id=1680 lang=python3
#
# [1680] Concatenation of Consecutive Binary Numbers
#

# @lc code=start
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10 ** 9 + 7
        res = ""
        for i in range(1, n + 1):
            b = bin(i)[2:]
            res += b
        return int(res, 2) % mod

# @lc code=end

