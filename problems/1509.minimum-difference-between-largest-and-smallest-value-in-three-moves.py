#
# @lc app=leetcode id=1509 lang=python3
# @lcpr version=
#
# [1509] Minimum Difference Between Largest and Smallest Value in Three Moves
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(nums[-4+i]-nums[i] for i in range(4))

# @lc code=end

print(Solution().minDifference([1,5,0,10,14]))

#
# @lcpr case=start
# [5,3,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,5,0,10,14]\n
# @lcpr case=end

# @lcpr case=start
# [3,100,20]\n
# @lcpr case=end

#

