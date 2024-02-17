#
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#

# @lc code=start
from functools import cache
import heapq
from typing import List

# Memory Limit Exceeded, 11 / 78 testcases passed
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        length = len(heights) - 1
        @cache
        def dp(i: int, bricks: int, ladders: int) -> int:
            # print(f"dp({i},{bricks},{ladders})")
            if i == length:
                return i 
            thisH = heights[i]
            nextH = heights[i+1]
            dh = max(nextH-thisH,0)
            if dh:
                return max(
                    dp(i+1, bricks-dh, ladders) if bricks>=dh else i, 
                    dp(i+1, bricks, ladders-1) if ladders else i, 
                )
            else: 
                return dp(i+1, bricks, ladders)
        return dp(0, bricks, ladders)

# Time Limit Exceeded, 72 / 78 testcases passed
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        length = len(heights) - 1
        i = 0 
        need_pass = []
        while i<length:
            # print({'i':i,'bricks':bricks,'ladders':ladders, 'need_pass': need_pass})
            dh = max(heights[i+1] - heights[i], 0)
            if dh:
                need_pass.append(dh)
                if bricks>=dh:
                    bricks -= dh 
                elif ladders:
                    max_dh = max(need_pass)
                    need_pass.pop(need_pass.index(max_dh))
                    bricks -= dh
                    bricks += max_dh
                    ladders -= 1
                else:
                    break 
            i += 1
        return i 

# Time Limit Exceeded, 72 / 78 testcases passed
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        dhs = [] 
        enum = enumerate(heights)
        _, last = next(enum)
        
        for i,v in enum:
            dh = max(v-last,0)
            if dh:
                dhs.append((dh,i))
            last = v
        dhs.reverse()
        print(dhs)
        passed = [] 
        max_i = 0
        while dhs:
            dh,i = dhs.pop()
            passed.append(dh)
            if bricks>=dh:
                bricks -= dh 
            elif ladders:
                max_dh = max(passed)
                passed.pop(passed.index(max_dh))
                bricks -= dh
                bricks += max_dh
                ladders -= 1
            else:
                dhs.append((dh,i)) 
                max_i = i-1
                break 
        if not dhs:
            return len(heights)-1
        return max_i 


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        passed = []
        i = 0 
        for i in range(len(heights)-1):
            dh = max(heights[i+1]-heights[i],0)
            if dh:
                bricks -= dh 
                heapq.heappush(passed, -dh)
                if bricks < 0: 
                    bricks -= heapq.heappop(passed)
                    ladders -= 1 
                if ladders < 0:
                    break 
        else:
            i = len(heights) - 1 
            # print(passed)
        return i

# @lc code=end

print(Solution().furthestBuilding([4,2,7,6,9,14,12],5,1))
print(Solution().furthestBuilding([4,12,2,7,3,18,20,3,19],10,2))
