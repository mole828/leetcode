#
# @lc app=leetcode id=407 lang=python3
# @lcpr version=30204
#
# [407] Trapping Rain Water II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from heapq import heapify, heappop, heappush
from typing import List

# 2025-10-03
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        h = []
        for i, row in enumerate(heightMap):
            for j, height in enumerate(row):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    h.append((height, i, j))
                    row[j] = -1  # 标记 (i,j) 访问过
        heapify(h)

        ans = 0
        while h:
            min_height, i, j = heappop(h)  # min_height 是木桶的短板
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                if 0 <= x < m and 0 <= y < n and heightMap[x][y] >= 0:  # (x,y) 没有访问过
                    # 如果 (x,y) 的高度小于 min_height，那么接水量为 min_height - heightMap[x][y]
                    ans += max(min_height - heightMap[x][y], 0)
                    # 给木桶新增一块高为 max(min_height, heightMap[x][y]) 的木板
                    heappush(h, (max(min_height, heightMap[x][y]), x, y))
                    heightMap[x][y] = -1  # 标记 (x,y) 访问过
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/trapping-rain-water-ii/solutions/2998212/duan-ban-xiao-ying-pythonjavacgojsrust-b-39mp/
  
# @lc code=end



#
# @lcpr case=start
# [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]\n
# @lcpr case=end

#

