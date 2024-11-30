#
# @lc app=leetcode id=2097 lang=python3
# @lcpr version=30204
#
# [2097] Valid Arrangement of Pairs
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter, defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        degree = Counter()
        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            degree[u] += 1
            degree[v] -= 1
        start = pairs[0][0]
        for node, deg in degree.items():
            if deg == 1:
                start = node

        def dfs(node: int) -> None:
            while graph[node]:
                nei = graph[node].pop()
                dfs(nei)
                result.append([node, nei])

        result = []
        dfs(start)
        return result[::-1]

# @lc code=end

print(Solution().validArrangement([[5,1],[4,5],[11,9],[9,4]]))

#
# @lcpr case=start
# [[5,1],[4,5],[11,9],[9,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3],[3,2],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[1,3],[2,1]]\n
# @lcpr case=end

#

