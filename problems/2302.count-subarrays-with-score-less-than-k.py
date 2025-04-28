#
# @lc app=leetcode id=2302 lang=python3
#
# [2302] Count Subarrays With Score Less Than K
#

# @lc code=start
from typing import List


class Solution:
    # Time Limit Exceeded, 150/167 cases passed
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                sub = nums[i:j + 1]
                point = sum(sub) * len(sub)
                if point < k:
                    ans += 1
                else:
                    break
        return ans
    # Time Limit Exceeded, 152/167 cases passed
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            sum_of_sub = 0
            for j in range(i, n):
                sum_of_sub += nums[j]
                point = sum_of_sub * (j-i+1)
                if point < k:
                    ans += 1
                else:
                    break
        return ans
    # Time Limit Exceeded, 151/167 cases passed
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            point = 0
            sum_of_sub = 0
            for j in range(i, n):
                sum_of_sub += nums[j]
                point += sum_of_sub + nums[j] * (j-i)
                if point < k:
                    ans += 1
                else:
                    break
        return ans

    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = s = left = 0
        for right, x in enumerate(nums):
            s += x
            while s * (right - left + 1) >= k:
                s -= nums[left]
                left += 1
            ans += right - left + 1
        return ans
# @lc code=end

print(Solution().countSubarrays([2,1,4,3,5], 10))