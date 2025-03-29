#
# @lc app=leetcode id=2033 lang=python3
#
# [2033] Minimum Operations to Make a Uni-Value Grid
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted(sum(grid, []))
        remain_set = set(num%x for num in nums)
        if len(remain_set) != 1:
            return -1
        subs = [num//x for num in nums]
        min_sub = subs[0]
        total = sum((sub-min_sub) for sub in subs)
        # print(subs, total)
        min_total = total
        n = len(nums)
        for i in range(1, n):
            dx = subs[i] - subs[i-1]
            total += dx * i
            total -= dx * (n - i)
            min_total = min(min_total, total)
        return min_total


        
# @lc code=end

print(Solution().minOperations(grid = [[2,4],[6,8]], x = 2))