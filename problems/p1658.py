from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        res = -1
        sum_nums = sum(nums)
        target = sum_nums - x
        left = 0
        subsum = 0
        for right in range(n):
            subsum += nums[right]
            while left <= right and subsum > target:
                subsum -= nums[left]
                left += 1
            if subsum == target:
                res = max(res, right - left + 1)
        return n - res if res >= 0 else -1