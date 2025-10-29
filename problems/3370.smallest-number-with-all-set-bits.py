#
# @lc app=leetcode id=3370 lang=python3
#
# [3370] Smallest Number With All Set Bits
#

# @lc code=start
class Solution:
    def smallestNumber(self, n: int) -> int:
        s = bin(n)
        s = '1' * (len(s) - 2)
        return int(s, 2)
# @lc code=end

