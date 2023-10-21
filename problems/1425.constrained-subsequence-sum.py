#
# @lc app=leetcode id=1425 lang=python3
#
# [1425] Constrained Subsequence Sum
#

# @lc code=start
import collections
from functools import cache
from typing import List

# cache 之后 Memory Limit Exceeded
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def dp(index: int, last: int) -> int:
            if index == n :
                return float('-inf') if last<0 else 0
            
            return max(
                nums[index] + dp(index+1, k) if last else 0,
                dp(index+1, last-1 if last else last)
            ) if last else 0
        
        return dp(index=0, last=-1)
        
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = nums[:1]
        decrease = collections.deque(dp)
        for i, x in enumerate(nums[1:], 1):
            if i > k and decrease[0] == dp[i - k - 1]:
                decrease.popleft()
                
            tmp = max(x, decrease[0] + x)
            dp += tmp,
            while decrease and decrease[-1] < tmp:
                decrease.pop()
            decrease += tmp, 
        return max(dp)  
            

# @lc code=end


print(Solution().constrainedSubsetSum(nums = [-1,-2,-3], k = 1))

print(Solution().constrainedSubsetSum(nums = [10,2,-10,5,20], k = 2))