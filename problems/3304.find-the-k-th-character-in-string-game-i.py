#
# @lc app=leetcode id=3304 lang=python3
#
# [3304] Find the K-th Character in String Game I
#

# @lc code=start
from cmath import log
from string import ascii_lowercase


class Solution:
    def kthCharacter(self, k: int) -> str:
        return ascii_lowercase[(k-1).bit_count()]
        
        
# @lc code=end

print(Solution().kthCharacter(7))