#
# @lc app=leetcode id=2200 lang=python3
#
# [2200] Find All K-Distant Indices in an Array
#

# @lc code=start
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = [False for _ in nums]
        for i,v in enumerate(nums):
            if v == key:
                for j in range(i-k, i+k+1):
                    if j >= 0 and j < len(nums):
                        ans[j] = True
        return [i for i,v in enumerate(ans) if v]
        
# @lc code=end

