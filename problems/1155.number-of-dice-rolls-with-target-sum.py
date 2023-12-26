#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#

# @lc code=start
from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def dp(lastTime: int, target: int)-> int:
            # print(f"dp({lastTime},{target})")
            if not lastTime:
                return 1 if 1<=target<=k else 0
            return sum(
                dp(lastTime-1, target-i)
                for i in range(1,k+1)
            ) 
        return dp(n-1,target) % (10**9+7)
                

# @lc code=end

print(Solution().numRollsToTarget(1,6,3))
print(Solution().numRollsToTarget(2,6,7))
print(Solution().numRollsToTarget(30,30,500))