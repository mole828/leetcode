#
# @lc app=leetcode id=1857 lang=python3
#
# [1857] Largest Color Value in a Directed Graph
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g: List[List[int]] = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in edges:
            if x == y:  # 自环
                return -1
            g[x].append(y)
            deg[y] += 1

        ans = visited = 0
        q = deque(i for i, d in enumerate(deg) if d == 0)  # 入度为 0 的点入队
        f: List[dict[str,int]] = [defaultdict(int) for _ in range(n)]
        while q:
            x = q.popleft()  # x 的所有转移来源都计算完毕，也都更新到 f[x] 中
            visited += 1
            ch = colors[x]
            f[x][ch] += 1
            ans = max(ans, f[x][ch])
            for y in g[x]:
                for ch, c in f[x].items():
                    f[y][ch] = max(f[y][ch], c)  # 刷表法，更新邻居的最大值
                deg[y] -= 1
                if deg[y] == 0:
                    q.append(y)

        return ans if visited == n else -1

# @lc code=end

print(Solution().largestPathValue(colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]))