#
# @lc app=leetcode id=3392 lang=python3
#
# [3392] Count Subarrays of Length Three With a Condition
#

# @lc code=start
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(2, len(nums)):
            a,b,c = nums[i-2:i+1]
            if a + c == b/2:
                ans += 1
        return ans

# @lc code=end

print(Solution().countSubarrays([-2,4,-2]))