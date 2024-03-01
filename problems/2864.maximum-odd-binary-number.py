#
# @lc app=leetcode id=2864 lang=python3
#
# [2864] Maximum Odd Binary Number
#

# @lc code=start
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one = s.count('1')
        return '1'*(one-1)+'0'*(len(s)-one)+'1'
# @lc code=end

