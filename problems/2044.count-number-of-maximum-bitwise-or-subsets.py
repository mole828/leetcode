#
# @lc app=leetcode id=2044 lang=python3
# @lcpr version=
#
# [2044] Count Number of Maximum Bitwise-OR Subsets
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import reduce
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = reduce(lambda x, y: x | y, nums)
        def dfs(i, cur):
            if i == len(nums):
                return cur == target
            return dfs(i+1, cur) + dfs(i+1, cur | nums[i])
        return dfs(0, 0)
        
# @lc code=end



#
# @lcpr case=start
# [3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,5]\n
# @lcpr case=end

#

