#
# @lc app=leetcode id=514 lang=python3
# @lcpr version=
#
# [514] Freedom Trail
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

import bisect
from collections import defaultdict, deque
from functools import cache

import numpy as np


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        '''
        理解错误
        '''
        step = 0
        que = deque(ring)
        for c in key:
            cr = que.popleft()
            while cr != c:
                que.append(cr)
                step += 1
                cr = que.popleft()
            step += 1
            que.appendleft(cr)
        return step
    
    def findRotateSteps(self, ring: str, key: str) -> int:
        '''
        "iotfo"
        "fioot"
        i 有两个 o 可以选的时候出现了错误
        '''
        ring_len = len(ring)
        index:dict[str, set[int]] = defaultdict(set)
        for i,c in enumerate(ring):
            index[c].add(i)
            index[c].add(i-ring_len)
            index[c].add(i+ring_len)
        step = 0
        i = 0
        for c in key:
            index[c]
            d,next_i = min((abs(i-j),j) for j in index[c])
            step += d + 1
            i = next_i%ring_len
        return step
    
    def findRotateSteps(self, ring: str, key: str) -> int:
        index:dict[str, set[int]] = defaultdict(set)
        for i,c in enumerate(ring):
            index[c].add(i)
            index[c].add(i-len(ring))
            index[c].add(i+len(ring))
        @cache
        def dp(ki: int, ri: int) -> int:
            if ki == len(key):
                return 0
            kc = key[ki]
            return min(dp(ki+1, i%len(ring))+abs(ri-i) for i in index[kc])+1
        return dp(0,0)
            
# @lc code=end

print(Solution().findRotateSteps("godding", "gd"))

#
# @lcpr case=start
# "godding"\n"gd"\n
# @lcpr case=end

# @lcpr case=start
# "godding"\n"godding"\n
# @lcpr case=end

#

