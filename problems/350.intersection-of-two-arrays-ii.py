#
# @lc app=leetcode id=350 lang=python3
# @lcpr version=
#
# [350] Intersection of Two Arrays II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        s = set(c1.keys()) and set(c2.keys())
        return Counter({k:min(c1[k],c2[k]) for k in s}).elements()
        
# @lc code=end

print(Solution().intersect([1,2,2,1], [2,2,]))

#
# @lcpr case=start
# [1,2,2,1]\n[2,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,5]\n[9,4,9,8,4]\n
# @lcpr case=end

#

