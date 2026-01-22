#
# @lc app=leetcode id=3507 lang=python3
#
# [3507] Minimum Pair Removal to Sort Array I
#

# @lc code=start
from itertools import pairwise
from typing import List

from sortedcontainers import SortedList


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        sl = SortedList() 
        idx = SortedList(range(len(nums))) 
        dec = 0  

        for i, (x, y) in enumerate(pairwise(nums)):
            if x > y:
                dec += 1
            sl.add((x + y, i))

        ans = 0
        while dec > 0:
            ans += 1

            s, i = sl.pop(0)  
            k = idx.bisect_left(i)

            nxt = idx[k + 1]
            if nums[i] > nums[nxt]: 
                dec -= 1

            if k > 0:
                pre = idx[k - 1]
                if nums[pre] > nums[i]:
                    dec -= 1
                if nums[pre] > s: 
                    dec += 1
                sl.remove((nums[pre] + nums[i], pre))
                sl.add((nums[pre] + s, pre))

            if k + 2 < len(idx):
                nxt2 = idx[k + 2]
                if nums[nxt] > nums[nxt2]:
                    dec -= 1
                if s > nums[nxt2]: 
                    dec += 1
                sl.remove((nums[nxt] + nums[nxt2], nxt))
                sl.add((s + nums[nxt2], i))

            nums[i] = s  
            idx.remove(nxt) 

        return ans
    
# @lc code=end

