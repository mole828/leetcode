#
# @lc app=leetcode id=494 lang=python3
# @lcpr version=
#
# [494] Target Sum
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def req(i: int, need: int) -> int:
            if i == len(nums):
                return 1 if need == 0 else 0
            return req(i+1, need-nums[i]) + req(i+1, need+nums[i])
        return req(0, target)
            
        
# @lc code=end



#
# @lcpr case=start
# [1,1,1,1,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

