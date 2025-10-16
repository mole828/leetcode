#
# @lc app=leetcode id=2598 lang=python3
#
# [2598] Smallest Missing Non-negative Integer After Operations
#

# @lc code=start
from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count = [0] * value
        for num in nums:
            count[num%value] += 1
        min_count = min(count)
        print(count, min_count)
        ans = min_count*value
        for i in range(value):
            if count[i] > min_count:
                ans += 1
            else:
                break
        return ans
        
# @lc code=end

