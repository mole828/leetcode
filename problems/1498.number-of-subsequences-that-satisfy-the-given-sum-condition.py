#
# @lc app=leetcode id=1498 lang=python3
# @lcpr version=30204
#
# [1498] Number of Subsequences That Satisfy the Given Sum Condition
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import bisect
from typing import List

MOD = 1_000_000_007
MX = 100_000

pow2 = [1] * MX  # pow2[i] = 2 ** i % MOD
for i in range(1, MX):
    pow2[i] = pow2[i - 1] * 2 % MOD

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] <= target:
                print(left, right, ans)
                ans += pow2[right - left]
                left += 1
            else:
                right -= 1
        return ans % MOD
# @lc code=end

print(Solution().numSubseq([3,5,6,7], 9))
print(Solution().numSubseq([3,3,6,8], 10))

#
# @lcpr case=start
# [3,5,6,7]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,3,6,8]\n10\n
# @lcpr case=end

# @lcpr case=start
# [2,3,3,4,6,7]\n12\n
# @lcpr case=end

#

