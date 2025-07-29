#
# @lc app=leetcode id=2411 lang=python3
#
# [2411] Smallest Subarrays With Maximum Bitwise OR
#

# @lc code=start
from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            cur = 0
            max_cur = float("-inf")
            min_len = float("inf")
            for j in range(i,n):
                cur |= nums[j]
                if cur > max_cur:
                    max_cur = cur
                    min_len = j - i + 1
            ans.append(min_len)
        return ans
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i,x in enumerate(nums):
            for j in range(i-1,-1,-1):
                if nums[j] | x == nums[j]:
                    break
                nums[j] |= x
                ans[j] = i - j + 1
        return ans
        
# @lc code=end

print(Solution().smallestSubarrays([1,0,2,1,3]))