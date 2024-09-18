#
# @lc app=leetcode id=179 lang=python3
# @lcpr version=
#
# [179] Largest Number
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # [99999991, 9] , 这种案例下, 9超过10个会出现 99..919 的错误情况
        # 但是测试用例 nums[i] 的范围是 0 <= nums[i] <= 10^9
        has_sort = sorted(nums, key=lambda x: str(x)*10, reverse=True)
        return str(int(''.join(map(str, has_sort))))
# @lc code=end



#
# @lcpr case=start
# [10,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,30,34,5,9]\n
# @lcpr case=end

#

