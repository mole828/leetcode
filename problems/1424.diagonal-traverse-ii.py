#
# @lc app=leetcode id=1424 lang=python3
#
# [1424] Diagonal Traverse II
#

# @lc code=start
from collections import defaultdict, deque
from itertools import chain
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = defaultdict(deque)
        for i, row in enumerate(nums):
            for j, x in enumerate(row):
                res[i + j].appendleft(x)
        return chain(*res.values())

# @lc code=end
print(Solution().findDiagonalOrder(
    nums = [[1,2,3],[4,5,6],[7,8,9]]
))
