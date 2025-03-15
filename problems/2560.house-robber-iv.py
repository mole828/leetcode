#
# @lc app=leetcode id=2560 lang=python3
# @lcpr version=30204
#
# [2560] House Robber IV
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
from typing import List


class Solution:
    # Time Limit Exceeded
    # 42/64 cases passed
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def dfs(i: int, last_take: int, last_chance: int) -> int:
            if last_chance == 0:
                return 0
            if i == n:
                return float('inf')
            pos = []
            if not last_take and last_chance:
                take = max( dfs(i+1, last_take=1, last_chance=last_chance-1) , nums[i])
                pos.append(take)
            not_take = dfs(i+1, last_take=0, last_chance=last_chance)
            pos.append(not_take)
            return min(pos) 
        return dfs(0,0,k)
    
    # Memory Limit Exceeded
    # 43/64 cases passed 
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        @cache
        def dfs(i: int, last_chance: int) -> int:
            if last_chance == 0:
                return 0
            if i >= n:
                return float('inf')
            return min(
                max( dfs(i+2, last_chance=last_chance-1) , nums[i] ),
                dfs(i+1, last_chance=last_chance),
            )
        return dfs(0, k)
    
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def check(mid: int):
            i = cnt = 0
            while i < n:
                if cnt == k: return True
                if nums[i] <= mid:
                    i += 2
                    cnt += 1
                else:
                    i += 1
            return cnt == k
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right)//2
            if check(mid): right = mid
            else: left = mid + 1
        return left

# @lc code=end

print(Solution().minCapability(nums = [2,3,5,9], k = 2))
print(Solution().minCapability(nums = [2,7,9,3,1], k = 2))
print(Solution().minCapability(nums = [3,2,3,2,], k = 5)) # k <= (len(nums)+1)//2

#
# @lcpr case=start
# [2,3,5,9]\n2\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n2\n
# @lcpr case=end

#

