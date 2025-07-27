#
# @lc app=leetcode id=2210 lang=python3
# @lcpr version=30204
#
# [2210] Count Hills and Valleys in an Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        a,b,c = nums[0], nums[1], nums[2]
        count = 0
        for i in range(2, len(nums)):
            c = nums[i]
            if (a<b>c) or (a>b<c):
                # print([a,b,c])
                count += 1
            if b != c:    
                a,b = b,c
        return count
# @lc code=end

print(Solution().countHillValley([2,4,1,1,6,5]))
print(Solution().countHillValley([6,6,5,5,4,1]))

#
# @lcpr case=start
# [2,4,1,1,6,5]\n
# @lcpr case=end

# @lcpr case=start
# [6,6,5,5,4,1]\n
# @lcpr case=end

#

