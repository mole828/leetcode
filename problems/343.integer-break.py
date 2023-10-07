#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2

        count_of_3s, remainder = divmod(n, 3)

        if remainder == 0:
            return 3 ** count_of_3s
        elif remainder == 1:
            return 3 ** (count_of_3s - 1) * 4
        else:  
            return 3 ** count_of_3s * 2
# @lc code=end

