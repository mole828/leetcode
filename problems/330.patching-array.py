#
# @lc app=leetcode id=330 lang=python3
# @lcpr version=
#
# [330] Patching Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        result = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                result += 1

        return result
# @lc code=end

print(Solution().minPatches([1,3],6))

#
# @lcpr case=start
# [1,3]\n6\n
# @lcpr case=end

# @lcpr case=start
# [1,5,10]\n20\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2]\n5\n
# @lcpr case=end

#

