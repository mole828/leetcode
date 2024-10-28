#
# @lc app=leetcode id=2501 lang=python3
# @lcpr version=
#
# [2501] Longest Square Streak in an Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        nums_set = set(nums)
        max_ans = -1
        for i,v in enumerate(nums):
            if v*v in nums_set:
                ans = 1
                while v*v in nums_set:
                    print(v*v, ans)
                    v *= v
                    ans += 1
                max_ans = max(ans, max_ans)
        return max_ans

        
# @lc code=end



#
# @lcpr case=start
# [4,3,6,16,8,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5,6,7]\n
# @lcpr case=end

#

