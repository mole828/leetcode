#
# @lc app=leetcode id=349 lang=python3
# @lcpr version=
#
# [349] Intersection of Two Arrays
#

# @lc code=start
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1)&set(nums2)
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n[2,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,5]\n[9,4,9,8,4]\n
# @lcpr case=end

#

