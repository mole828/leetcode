#
# @lc app=leetcode id=442 lang=python3
# @lcpr version=
#
# [442] Find All Duplicates in an Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        once = set() 
        twice = set() 
        for num in nums:
            if num in once:
                twice.add(num) 
            once.add(num) 
        return twice
        
# @lc code=end



#
# @lcpr case=start
# [4,3,2,7,8,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

