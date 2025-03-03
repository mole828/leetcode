#
# @lc app=leetcode id=2161 lang=python3
# @lcpr version=30204
#
# [2161] Partition Array According to Given Pivot
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        equal = []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                equal.append(num)
        return left + equal + right
        
# @lc code=end



#
# @lcpr case=start
# [9,12,5,10,14,3,10]\n10\n
# @lcpr case=end

# @lcpr case=start
# [-3,4,3,2]\n2\n
# @lcpr case=end

#

