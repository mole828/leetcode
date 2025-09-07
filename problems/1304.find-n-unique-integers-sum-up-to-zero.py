#
# @lc app=leetcode id=1304 lang=python3
# @lcpr version=30204
#
# [1304] Find N Unique Integers Sum up to Zero
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        r = n // 2
        ans = []
        for i in range(1, r + 1):
            ans.append(i)
            ans.append(-i)
        if n % 2 == 1:
            ans.append(0)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

