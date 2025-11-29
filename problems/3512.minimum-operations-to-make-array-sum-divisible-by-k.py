#
# @lc app=leetcode id=3512 lang=python3
# @lcpr version=30204
#
# [3512] Minimum Operations to Make Array Sum Divisible by K
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(iter(nums)) % k
# @lc code=end



#
# @lcpr case=start
# [3,9,7]\n5\n
# @lcpr case=end

# @lcpr case=start
# [4,1,3]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2]\n6\n
# @lcpr case=end

#

