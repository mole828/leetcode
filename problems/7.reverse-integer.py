#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        num = ''.join(reversed(str(abs(x))))
        sub = '-' if x < 0 else ''
        print(sub, num)
        y = int(sub+num)
        return y if -2**31 <= y <= 2**31 else 0 
# @lc code=end

