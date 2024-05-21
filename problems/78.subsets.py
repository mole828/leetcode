#
# @lc app=leetcode id=78 lang=python3
# @lcpr version=
#
# [78] Subsets
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = []
        def dp(i: int, sub: List[int]):
            if i == len(nums):
                subs.append(sub)
                return
            dp(i+1, sub)
            dp(i+1, sub+[nums[i]])
        dp(0,[])
        return subs
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

