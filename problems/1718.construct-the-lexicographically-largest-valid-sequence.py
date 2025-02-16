#
# @lc app=leetcode id=1718 lang=python3
# @lcpr version=30204
#
# [1718] Construct the Lexicographically Largest Valid Sequence
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from typing import List, Optional 


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2*n-1)
        used = [0] * (n+1)

        def dfs(i: int):
            if i == 2*n-1:
                return True
            if ans[i] != 0:
                return dfs(i+1)
            for x in range(n, 0, -1):
                if used[x]:
                    continue
                if x == 1:
                    used[x] = ans[i] = x
                    if dfs(i+1):
                        return True
                    used[x] = ans[i] = 0
                elif i+x < 2*n-1 and ans[i+x] == 0:
                    ans[i] = ans[i+x] = used[x] = x
                    if dfs(i+1):
                        return True
                    ans[i] = ans[i+x] = used[x] = 0
            return False
        dfs(0)
        return ans
            
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

#

