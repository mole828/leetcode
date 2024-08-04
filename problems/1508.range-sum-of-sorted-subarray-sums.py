#
# @lc app=leetcode id=1508 lang=python3
# @lcpr version=
#
# [1508] Range Sum of Sorted Subarray Sums
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

MOD = 10**9+7
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sum_of_subs = []
        for l in range(len(nums)):
            for r in range(l, len(nums)):
                sub = nums[l:r+1]
                sum_of_subs.append(sum(sub))
        sum_of_subs.sort()
        print(sum_of_subs)
        return sum(sum_of_subs[left-1:right])%MOD
# @lc code=end

print(Solution().rangeSum([1,2,3,4],4,1,5))

#
# @lcpr case=start
# [1,2,3,4]\n4\n1\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n4\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n4\n1\n10\n
# @lcpr case=end

#

