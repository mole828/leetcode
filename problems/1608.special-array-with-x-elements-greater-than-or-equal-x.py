#
# @lc app=leetcode id=1608 lang=python3
# @lcpr version=30202
#
# [1608] Special Array With X Elements Greater Than or Equal X
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        bucket = [0] * 1001
        for num in nums:
            bucket[num] += 1
        total = len(nums)
        for i in range(1001):
            if i == total:
                return i
            total -= bucket[i]
        return -1
# @lc code=end



#
# @lcpr case=start
# [3,5]\n
# @lcpr case=end

# @lcpr case=start
# [0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,4,3,0,4]\n
# @lcpr case=end

#

