#
# @lc app=leetcode id=386 lang=python3
# @lcpr version=
#
# [386] Lexicographical Numbers
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        def dfs(x: int = 1):
            if x > n:
                return
            result.append(x)
            for i in range(10):
                dfs(x * 10 + i)
        for i in range(1, 10):
            dfs(i)

        return result
# @lc code=end



#
# @lcpr case=start
# 13\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

