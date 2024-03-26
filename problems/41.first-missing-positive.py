#
# @lc app=leetcode id=41 lang=python3
# @lcpr version=
#
# [41] First Missing Positive
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int: 
        sub = set(range(1,len(nums)+2))-set(nums)
        print(sub)
        return sorted(sub)[0]
    
# O(1) space 
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int: 
        nums.sort() 
        next_num = 1
        for num in nums: 
            if num == next_num:
                next_num += 1
            elif num > next_num:
                return next_num
        return next_num
# @lc code=end



#
# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#

