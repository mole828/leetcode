from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def cnt(nums):
            n = len(nums)
            ans = 0
            for i in range(1,n,2):
                if i + 1 < n:
                    temp = min(nums[i-1],nums[i+1])
                    ans += nums[i] - temp + 1 if nums[i] >= temp else 0
                if i + 1 == n and nums[i-1] <= nums[i]:
                    ans += nums[i] - nums[i-1] + 1
            return ans
        return min(cnt(nums),cnt([float('inf')] + nums))