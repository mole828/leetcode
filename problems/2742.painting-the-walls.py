#
# @lc app=leetcode id=2742 lang=python3
#
# [2742] Painting the Walls
#

# @lc code=start
from functools import lru_cache
from typing import List

# not pass 
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        cts = sorted(tuple([-ct[-1]/ct[0],*ct]) for ct in zip(cost, time))
        print(cts)
        ans = 0
        while cts:
            paid_ct = cts.pop(0)
            for _ in range(paid_ct[-1]):
                if cts:
                    cts.pop()
            ans += paid_ct[1]
        return ans
    
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # maxsize=2**17 time limit
        # maxsize=2**18 memory limit 
        @lru_cache(maxsize=2**17)
        def dp(index: int, time_cost: int) -> int:
            if index == len(cost):
                return float('inf') if time_cost<0 else 0
            return min(
                cost[index] + dp(index=index+1, time_cost=time_cost+time[index]),
                dp(index=index+1, time_cost=time_cost-1)
            )
        return dp(0,0)

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(index: int, time_cost: int) -> int:
            if index == len(cost):
                return float('inf') if time_cost<0 else 0
            if time_cost >= len(cost) - index:
                return 0
            return min(
                cost[index] + dp(index=index+1, time_cost=time_cost+time[index]),
                dp(index=index+1, time_cost=time_cost-1)
            )
        return dp(0,0)
        

# @lc code=end

assert Solution().paintWalls(cost = [1,2,3,2], time = [1,2,3,2]) == 3

assert Solution().paintWalls(cost = [26,53,10,24,25,20,63,51], time = [1,1,1,1,2,2,2,1]) == 55
