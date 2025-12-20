#
# @lc app=leetcode id=944 lang=python3
#
# [944] Delete Columns to Make Sorted
#

# @lc code=start
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for col in zip(*strs):
            if list(col) != sorted(col):
                ans += 1
        return ans
        
# @lc code=end

