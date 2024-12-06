#
# @lc app=leetcode id=2554 lang=python3
# @lcpr version=
#
# [2554] Maximum Number of Integers to Choose From a Range I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        total_sum = 0
        ans = 0
        for i in range(1, n+1):
            if i in banned:
                continue
            total_sum += i
            if total_sum > maxSum:
                break
            ans += 1
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [1,6,5]\n5\n6\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7]\n8\n1\n
# @lcpr case=end

# @lcpr case=start
# [11]\n7\n50\n
# @lcpr case=end

#

