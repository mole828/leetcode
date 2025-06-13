#
# @lc app=leetcode id=2616 lang=python3
#
# [2616] Minimize the Maximum Difference of Pairs
#

# @lc code=start
from bisect import bisect_left
from functools import cache
from typing import List


class Solution:
    # Memory Limit Exceeded, 1572 / 1582 testcases passed
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        diff: list[int] = []
        for i in range(len(nums)-1):
            diff.append(nums[i+1]-nums[i])
        @cache
        def dfs(i: int, last_pick: bool, pick_times: int) -> int:
            if i >= len(diff):
                return 0 if pick_times == 0 else 10**10
            ans = dfs(i+1, False, pick_times)
            if not last_pick:
                ans = min(ans, max(dfs(i+1, True, pick_times-1), diff[i]))
            return ans
        return dfs(0, False, p)
    
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        _max, _min = nums[-1], nums[0]
        
        for i in range(len(nums)-1):
            nums[i] = nums[i+1]-nums[i]

        def check(mx: int) -> int:
            cnt = i = 0
            while i < len(nums) - 1:
                if nums[i] <= mx:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p
        return bisect_left(range(_max - _min), True, key=check)
        
# @lc code=end

print(Solution().minimizeMax([10,1,2,7,1,3], 2))