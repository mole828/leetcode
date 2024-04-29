#
# @lc app=leetcode id=2997 lang=python3
# @lcpr version=
#
# [2997] Minimum Number of Operations to Make Array XOR Equal to K
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import reduce
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for num in nums:
            k ^= num
        return k.bit_count()
# @lc code=end

print(Solution().minOperations([2,1,3,4], 1))

#
# @lcpr case=start
# [2,1,3,4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,0,2,0]\n0\n
# @lcpr case=end

#

