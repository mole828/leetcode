#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from collections import defaultdict
from typing import Dict, List
class Solution:
    def _threeSum(self, nums: List[int]) -> List[List[int]]:
        has1:dict[int, int] = {} 
        has2 = defaultdict(set[tuple[int,int]])
        ans = []
        for i in range(len(nums)):
            num = nums[i]
            if -num in has2:
                for a,b in has2[-num]:
                    ans.append([a,b,i])
            for num1 in has1:
                has2[num+num1].add((has1[num1], i))
            has1[num] = i 
        return list(set(tuple(sorted([nums[a],nums[b],nums[c]])) for a,b,c in ans))
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        set1: set[int] = set()
        index2: dict[int, set[tuple[int, int]]] = defaultdict(set)
        ans:set[tuple[int,int,int]] = set()
        for num in nums:
            if -num in index2:
                for a,b in index2[-num]:
                    ans.add(tuple(sorted([num,a,b])))
            for a in set1:
                index2[a+num].add(tuple([a,num]))
            set1.add(num)
        return [list(s) for s in ans]
# @lc code=end

print(Solution().threeSum([-1,0,1,2,-1,-4]))