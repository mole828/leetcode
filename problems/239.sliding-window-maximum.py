#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from typing import List

from sortedcontainers import SortedList


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return [
            max(nums[i : i + k]) for i in range(len(nums) - k + 1)
        ]
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        window = nums[:k]
        sorted_window = SortedList(window)
        ans.append(sorted_window[-1])
        for i in range(k, len(nums)):
            sorted_window.remove(nums[i - k])
            sorted_window.add(nums[i])
            ans.append(sorted_window[-1])
        return ans

# @lc code=end

