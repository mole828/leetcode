#
# @lc app=leetcode id=2300 lang=python3
# @lcpr version=30204
#
# [2300] Successful Pairs of Spells and Potions
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for spell in spells:
            l, r = 0, len(potions) - 1
            while l <= r:
                mid = (l + r) // 2
                if spell * potions[mid] >= success:
                    r = mid - 1
                else:
                    l = mid + 1
            res.append(len(potions) - l)
        return res
        
# @lc code=end



#
# @lcpr case=start
# [5,1,3]\n[1,2,3,4,5]\n7\n
# @lcpr case=end

# @lcpr case=start
# [3,1,2]\n[8,5,8]\n16\n
# @lcpr case=end

#

