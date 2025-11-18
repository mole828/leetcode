#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#

# @lc code=start
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        last = False
        while i < len(bits):
            value = bits[i]
            if value == 0:
                i += 1
                last = True
            else:
                i += 2
                last = False
        return last
            
# @lc code=end

