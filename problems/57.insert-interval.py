#
# @lc app=leetcode id=57 lang=python3
# @lcpr version=
#
# [57] Insert Interval
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

a2b = tuple[int,int]

class Solution:
    def insert(self, intervals: List[a2b], newInterval: a2b) -> List[a2b]:
        new_a, new_b = newInterval
        merged = []
        i = 0
        while i<len(intervals):
            a,b = intervals[i]
            if b >= new_a:
                break 
            merged.append((a,b))
            i += 1
        while i<len(intervals):
            a,b = intervals[i]
            if a > new_b:
                break 
            new_a = min(new_a,a)
            new_b = max(new_b,b)
            i += 1
        merged.append((new_a,new_b))
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        return merged


        
# @lc code=end



#
# @lcpr case=start
# [[1,3],[6,9]]\n[2,5]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[3,5],[6,7],[8,10],[12,16]]\n[4,8]\n
# @lcpr case=end

#

