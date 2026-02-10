#
# @lc app=leetcode id=3719 lang=python3
#
# [3719] Longest Balanced Subarray I
#

# @lc code=start
from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0

        for left in range(len(nums)):
            count = [set(), set()]
            for right in range(left, len(nums)):
                num = nums[right]
                count[num%2].add(num)
                if len(count[0]) == len(count[1]):
                    ans = max(ans, right-left+1)

        return ans

# @lc code=end

