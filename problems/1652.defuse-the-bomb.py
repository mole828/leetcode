#
# @lc app=leetcode id=1652 lang=python3
# @lcpr version=
#
# [1652] Defuse the Bomb
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        full_space = code * 2
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        for i in range(n):
            if k > 0:
                ans[i] = sum(full_space[i+1:i+k+1])
            else:
                ans[i] = sum(full_space[i+k+n:i+n])
        return ans

        
# @lc code=end



#
# @lcpr case=start
# [5,7,1,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,4,9,3]\n-2\n
# @lcpr case=end

#

