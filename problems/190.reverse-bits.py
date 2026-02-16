#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        binary = binary.zfill(32)
        reversed_binary = binary[::-1]
        return int(reversed_binary, 2)
# @lc code=end

