#
# @lc app=leetcode id=2425 lang=python3
# @lcpr version=
#
# [2425] Bitwise XOR of All Pairings
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        nums = nums1*(len(nums2)%2) + nums2*(len(nums1)%2)
        for i in nums:
            res ^= i
        return res
# @lc code=end

print(Solution().xorAllNums([2,1,3], [10,2,5,0]))  # 13
print(Solution().xorAllNums([1,2], [3,4]))  # 0

#
# @lcpr case=start
# [2,1,3]\n[10,2,5,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[3,4]\n
# @lcpr case=end

#

