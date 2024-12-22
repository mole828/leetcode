#
# @lc app=leetcode id=2940 lang=python3
# @lcpr version=30204
#
# [2940] Find Building Where Alice and Bob Can Meet
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from heapq import heappop, heappush
from typing import List


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        qs = [[] for _ in range(len(heights))]
        for i, query in enumerate(queries):
            query.sort()
            x, y = query
            if heights[x] < heights[y] or x == y:
                ans[i] = y
            else:
                qs[y].append((heights[x], i))
        
        h = []
        for i, height in enumerate(heights):
            while h and h[0][0] < height:
                ans[heappop(h)[1]] = i
            for q in qs[i]:
                heappush(h, q)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [6,4,8,5,2,7]\n[[0,1],[0,3],[2,4],[3,4],[2,2]]\n
# @lcpr case=end

# @lcpr case=start
# [5,3,8,2,6,1,4,6]\n[[0,7],[3,5],[5,2],[3,0],[1,6]]\n
# @lcpr case=end

#

