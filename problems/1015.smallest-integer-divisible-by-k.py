#
# @lc app=leetcode id=1015 lang=python3
#
# [1015] Smallest Integer Divisible by K
#

# @lc code=start
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        has = set()
        x = 1 % k
        while x and x not in has:
            has.add(x)
            x = (x * 10 + 1) % k
        return len(has) + 1 if x == 0 else -1

# @lc code=end

