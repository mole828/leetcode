#
# @lc app=leetcode id=3160 lang=python3
# @lcpr version=30204
#
# [3160] Find the Number of Distinct Colors Among the Balls
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from typing import List


# Memory Limit Exceeded
# 547/551 cases passed (N/A)
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * (limit + 1)
        ans = []
        for i, j in queries:
            colors[i] = j
            s = set(colors) - {0}
            ans.append(len(s))
        return ans
        

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = {}
        color_count = defaultdict(int)
        ans = []
        for i, j in queries:
            if colors.get(i, None):
                color_count[colors[i]] -= 1
                if color_count[colors[i]] == 0:
                    del color_count[colors[i]]
            colors[i] = j
            color_count[j] += 1
            ans.append(len(color_count))
        return ans

# @lc code=end



#
# @lcpr case=start
# 4\n[[1,4],[2,5],[1,3],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[0,1],[1,2],[2,2],[3,4],[4,5]]\n
# @lcpr case=end

#

