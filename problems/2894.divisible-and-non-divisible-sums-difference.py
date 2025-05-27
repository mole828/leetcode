#
# @lc app=leetcode id=2894 lang=python3
#
# [2894] Divisible and Non-divisible Sums Difference
#

# @lc code=start
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        y = 0
        for x in range(n+1):
            y += x if x % m else -x
        return y

# @lc code=end

