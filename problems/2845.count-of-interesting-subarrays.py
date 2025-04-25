#
# @lc app=leetcode id=2845 lang=python3
#
# [2845] Count of Interesting Subarrays
#

# @lc code=start
from typing import List

class Solution:
    # Time Limit Exceeded, 609 / 617 testcases passed 
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ans = 0
        n = len(nums)
        for left in range(n):
            for right in range(left + 1, n + 1):
                sub = nums[left:right]
                cnt = sum(1 for v in sub if v % modulo == k)
                if cnt % modulo == k:
                    ans += 1
        return ans
    # Time Limit Exceeded, 609 / 617 testcases passed 
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ans = 0
        n = len(nums)
        for left in range(n):
            cnt = 0
            for right in range(left, n):
                num = nums[right]
                cnt += num % modulo == k
                if cnt % modulo == k:
                    ans += 1
        return ans
    
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        cnt = [0] * min(len(nums) + 1, modulo)
        cnt[0] = 1 
        ans = s = 0
        for x in nums:
            if x % modulo == k:
                s += 1
            if s >= k:
                ans += cnt[(s - k) % modulo]
            cnt[s % modulo] += 1
        return ans

# @lc code=end

print(Solution().countInterestingSubarrays([3,2,4], 2, 1))