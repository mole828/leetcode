#
# @lc app=leetcode id=523 lang=python3
# @lcpr version=
#
# [523] Continuous Subarray Sum
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map = {0: -1}
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k
            if rem in map:
                if i - map[rem] > 1:
                    return True
            else:
                map[rem] = i

        return False
# @lc code=end

print(Solution().checkSubarraySum([23,2,4,6,7], 13))
print(Solution().checkSubarraySum([2,4,3], 6))

#
# @lcpr case=start
# [23,2,4,6,7]\n6\n
# @lcpr case=end

# @lcpr case=start
# [23,2,6,4,7]\n6\n
# @lcpr case=end

# @lcpr case=start
# [23,2,6,4,7]\n13\n
# @lcpr case=end

#

