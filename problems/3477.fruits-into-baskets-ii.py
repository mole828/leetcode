#
# @lc app=leetcode id=3477 lang=python3
#
# [3477] Fruits Into Baskets II
#

# @lc code=start
from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        baskets_not_used = [1] * len(baskets)
        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if baskets_not_used[i]:
                    if basket >= fruit:
                        baskets_not_used[i] = 0
                        break
        return sum(baskets_not_used)
    
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if basket >= fruit:
                    baskets[i] = 0
                    break
        return sum(1 for b in baskets if b)
# @lc code=end

