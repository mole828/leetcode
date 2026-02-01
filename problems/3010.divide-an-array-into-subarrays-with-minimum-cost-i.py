#
# @lc app=leetcode id=3010 lang=python3
#
# [3010] Divide an Array Into Subarrays With Minimum Cost I
#

# @lc code=start
from typing import List

from numpy import inf


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def dfs(index: int, time: int) -> int:
            if index >= len(nums):
                return inf
            cost = nums[index]
            if time == 0:
                return cost
            it = (
                dfs(next_index, time - 1) + cost
                for next_index in range(index + 1, len(nums) + 1)
            )
            return min(it, default=0) if time > 0 else inf
        return dfs(0, 2)
# @lc code=end

if __name__ == "__main__":
    print(Solution().minimumCost([1, 2, 3, 4, 5]))