#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start

from collections import defaultdict
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        set1: set[int] = set()
        index2: dict[int, set[tuple[int, int]]] = defaultdict(set)
        index3: dict[int, set[tuple[int, int, int]]] = defaultdict(set)
        ans: set[tuple[int,int,int,int]] = set()
        for num in nums:
            if target-num in index3:
                for a,b,c in index3[target-num]:
                    ans.add(tuple(sorted([a,b,c,num])))
            for key in index2:
                for a,b in index2[key]:
                    index3[num+key].add(tuple(sorted([num,a,b])))
            for a in set1:
                index2[num+a].add( tuple(sorted([num,a])) )
            set1.add(num)
        # print(set1, index2, index3, ans)
        return [list(s) for s in ans]

# @lc code=end

print(Solution().fourSum(nums = [1,0,-1,0,-2,2], target = 0))

