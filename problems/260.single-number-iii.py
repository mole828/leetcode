#
# @lc app=leetcode id=260 lang=python3
# @lcpr version=
#
# [260] Single Number III
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        has: set[int] = set()
        single: set[int] = set()
        for num in nums:
            if num in single:
                single.remove(num)
                has.add(num)
            if num not in has:
                single.add(num)
        return single
            
        
# @lc code=end



#
# @lcpr case=start
# [1,2,1,3,2,5]\n
# @lcpr case=end

# @lcpr case=start
# [-1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

#

