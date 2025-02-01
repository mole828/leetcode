#
# @lc app=leetcode id=3151 lang=python3
# @lcpr version=30204
#
# [3151] Special Array I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        last = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            if (x - last)%2 == 0:
                return False
            last = x
        return True
        
# @lc code=end



#
# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,1,6]\n
# @lcpr case=end

#

