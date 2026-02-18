#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)[2:]
        for i in range(1, len(b)):
            if b[i] == b[i-1]:
                return False
        return True
# @lc code=end

