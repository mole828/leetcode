#
# @lc app=leetcode id=3190 lang=python3
# @lcpr version=30204
#
# [3190] Find Minimum Operations to Make All Elements Divisible by Three
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 for num in nums if num % 3 != 0)
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,6,9]\n
# @lcpr case=end

#

