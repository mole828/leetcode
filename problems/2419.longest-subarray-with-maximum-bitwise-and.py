#
# @lc app=leetcode id=2419 lang=python3
# @lcpr version=
#
# [2419] Longest Subarray With Maximum Bitwise AND
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        ans = cnt = 0
        for x in nums:
            if x == mx:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans

        
# @lc code=end

print( 0 & 3 )

#
# @lcpr case=start
# [1,2,3,3,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

#

