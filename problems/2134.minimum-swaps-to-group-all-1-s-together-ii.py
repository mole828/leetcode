#
# @lc app=leetcode id=2134 lang=python3
# @lcpr version=
#
# [2134] Minimum Swaps to Group All 1's Together II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = sum(nums)
        if cnt == 0:
            return 0
        
        cur = 0
        for i in range(cnt):
            cur += (1 - nums[i])
        
        ans = cur
        for i in range(1, n):
            if nums[i - 1] == 0:
                cur -= 1
            if nums[(i + cnt - 1) % n] == 0:
                cur += 1
            ans = min(ans, cur)
        return ans

# @lc code=end



#
# @lcpr case=start
# [0,1,0,1,1,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1,0,0,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,0,0,1]\n
# @lcpr case=end

#

