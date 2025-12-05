#
# @lc app=leetcode id=3432 lang=python3
# @lcpr version=30204
#
# [3432] Count Partitions with Even Sum Difference
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        ans = 0
        for i in range(len(nums)-1):
            num = nums[i]
            right -= num
            left += num
            d = left - right
            print(left, right, d)
            if d % 2 == 0:
                ans += 1
        return ans
        
# @lc code=end

print(Solution().countPartitions([10,10,3,7,6]))  # Expected output: 4

#
# @lcpr case=start
# [10,10,3,7,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6,8]\n
# @lcpr case=end

#

