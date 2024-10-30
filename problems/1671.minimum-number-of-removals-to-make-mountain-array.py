#
# @lc app=leetcode id=1671 lang=python3
# @lcpr version=30204
#
# [1671] Minimum Number of Removals to Make Mountain Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import bisect
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        ln = len(nums)
        rev = [1] * ln
        picked = [nums[-1]]
        for i in range(ln-2, 0, -1):
            n = nums[i]
            if n > picked[-1]:
                picked.append(n)
            else:
                picked[bisect.bisect_left(picked, n)] = n
            rev[i] = len(picked)
        ans, picked = 0, [nums[0]]
        for i in range(1, ln-1):
            n = nums[i]
            if n > picked[-1]:
                picked.append(n)
            else:
                picked[bisect.bisect_left(picked, n)] = n
            if len(picked) > 1 and rev[i] > 1:
                ans = max(len(picked)+rev[i]-1, ans)
        return ln - ans
        
# @lc code=end



#
# @lcpr case=start
# [1,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,1,5,6,2,3,1]\n
# @lcpr case=end

#

