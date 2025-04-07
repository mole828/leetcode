#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum_of_nums = sum(nums)
        if sum_of_nums % 2 == 1:
            return False
        @cache
        def dfs(index: int, last_sum: int) -> bool:
            if last_sum == 0:
                return True
            if last_sum < 0:
                return False
            if index == n:
                return False
            return dfs(index + 1, last_sum - nums[index]) or dfs(index + 1, last_sum)
        return dfs(0, sum_of_nums // 2)
# @lc code=end

print(Solution().canPartition([1, 5, 11, 5]))
print(Solution().canPartition([1, 2, 3, 5]))