#
# @lc app=leetcode id=2145 lang=python3
#
# [2145] Count the Hidden Sequences
#

# @lc code=start
from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_stats = 0
        max_stats = 0
        state = 0
        for diff in differences:
            state += diff
            min_stats = min(min_stats, state)
            max_stats = max(max_stats, state)
        diff_from_low = min_stats - lower
        max_stats -= diff_from_low
        last = upper - max_stats
        return max(last + 1, 0)
            
        
# @lc code=end

print(Solution().numberOfArrays(differences = [1,-3,4], lower = 1, upper = 6))