#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        while n:
            while not n%2 and n>0:
                n>>=1
            n -= 1
            output += 1
        return output
# @lc code=end

print(Solution().hammingWeight(11))
