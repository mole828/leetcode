#
# @lc app=leetcode id=2433 lang=python3
#
# [2433] Find The Original Array of Prefix Xor
#

# @lc code=start
from functools import cache, reduce
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [pref[i] ^ pref[i-1] for i in range(1, len(pref))]
# @lc code=end
print(Solution().findArray(pref = [5,2,0,3,1]))

