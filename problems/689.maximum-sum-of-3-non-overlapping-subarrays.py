#
# @lc app=leetcode id=689 lang=python3
# @lcpr version=30204
#
# [689] Maximum Sum of 3 Non-Overlapping Subarrays
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window = sum(nums[:k])
        left = [0] * (n - k + 1)
        left[0] = window
        for i in range(1, n - k + 1):
            window += nums[i + k - 1] - nums[i - 1]
            left[i] = window
        print(left)
        @cache
        def dp(i: int = 0, last_time: int = 3) -> tuple[int, list[int]]:
            if i >= len(left):
                return 0, []
            if last_time == 0:
                return 0, []
            pick = dp(i + k, last_time - 1)
            skip = dp(i + 1, last_time)
            if pick[0] + left[i] >= skip[0]:
                return pick[0] + left[i], [i] + pick[1]
            return skip
        return dp()[1]
        
# @lc code=end

print(Solution().maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2))

#
# @lcpr case=start
# [1,2,1,2,6,7,5,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2,1,2,1,2,1]\n2\n
# @lcpr case=end

#

