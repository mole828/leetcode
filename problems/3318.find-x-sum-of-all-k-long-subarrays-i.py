#
# @lc app=leetcode id=3318 lang=python3
#
# [3318] Find X-Sum of All K-Long Subarrays I
#

# @lc code=start
from collections import defaultdict
from typing import Counter, List

from sortedcontainers import SortedList


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        window = SortedList()
        window_count = defaultdict(int)
        def change_count(num: int, delta: int):
            old_tup = (-window_count[num], -num)
            if old_tup in window:
                window.remove(old_tup)
            window_count[num] += delta
            new_tup = (-window_count[num], -num)
            window.add(new_tup)

        for i,v in enumerate(nums[:k]):
            change_count(v, 1)
        
        def get_x_sum():
            ans = 0
            for i in range(min(x, len(window))):
                freq, val = window[i]
                ans += freq * val
            return ans
        
        ans = [get_x_sum()]
        for i in range(n - k):
            change_count(nums[i], -1)
            change_count(nums[i + k], 1)
            ans.append(get_x_sum())
        return ans
        
# @lc code=end

print(Solution().findXSum(nums=[1,1,2,2,3,4,2,3], k=6, x=2))