#
# @lc app=leetcode id=762 lang=python3
#
# [762] Prime Number of Set Bits in Binary Representation
#

# @lc code=start
primes = {2, 3, 5, 7, 11, 13, 17, 19}

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for x in range(left, right + 1):
            if x.bit_count() in primes:
                ans += 1
        return ans
# @lc code=end

