#
# @lc app=leetcode id=2050 lang=python3
#
# [2050] Parallel Courses III
#

# @lc code=start
from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]

        for prev, next in relations:
            graph[prev - 1].append(next - 1)

        @cache
        def dfs(index: int):
            return time[index] + max([dfs(i) for i in graph[index]],default=0)

        return max(dfs(i) for i in range(n))

            
# @lc code=end

print(
    Solution().minimumTime(
        n = 5, 
        relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], 
        time = [1,2,3,4,5]
    )
)