#
# @lc app=leetcode id=912 lang=python3
# @lcpr version=
#
# [912] Sort an Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# sorted pass

# Time Limit Exceeded, 10/21 cases passed (N/A)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def min_index()->int:
            min_i = -1
            min_v = float('inf')
            for i,v in enumerate(nums):
                if v < min_v:
                    min_i = i
                    min_v = v
            return min_i
        result = []
        while nums:
            result.append(nums.pop(min_index()))
        return result
# @lc code=end



#
# @lcpr case=start
# [5,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [5,1,1,2,0,0]\n
# @lcpr case=end

#

