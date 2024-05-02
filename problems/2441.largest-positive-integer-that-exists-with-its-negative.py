#
# @lc app=leetcode id=2441 lang=python3
# @lcpr version=
#
# [2441] Largest Positive Integer That Exists With Its Negative
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        while s:
            m = max(s)
            if -m in s:
                return m
            s.remove(m)
        return -1
        
# @lc code=end



#
# @lcpr case=start
# [-1,2,-3,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1,10,6,7,-7,1]\n
# @lcpr case=end

# @lcpr case=start
# [-10,8,6,7,-2,-3]\n
# @lcpr case=end

#

