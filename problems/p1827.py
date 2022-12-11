from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        less = nums[0]
        for num in nums:
            d = max(less-num, 0)
            ans += d
            less = num + d +1
        return ans