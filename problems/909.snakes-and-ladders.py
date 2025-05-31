#
# @lc app=leetcode id=909 lang=python3
# @lcpr version=30204
#
# [909] Snakes and Ladders
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        line = []
        for i in range(n:=len(board)):
            if i % 2 == 0:
                line.extend(board[n - 1 - i])
            else:
                line.extend(board[n - 1 - i][::-1])
        n = len(line)
        # print(line)
        MAX_STEP = 6
        que = [(0, 0)]
        heapq.heapify(que)
        visited = [False] * (n)
        while que:
            step, idx = heapq.heappop(que)
            if idx == n - 1:
                return step
            if visited[idx]:
                continue
            visited[idx] = True
            for i in range(1, MAX_STEP + 1):
                next_idx = idx + i
                if next_idx >= n:
                    break
                if line[next_idx] == -1:
                    heapq.heappush(que, (step + 1, next_idx))
                else:
                    heapq.heappush(que, (step + 1, line[next_idx] - 1))
        return -1


        
# @lc code=end

print(Solution().snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))

#
# @lcpr case=start
# [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]\n
# @lcpr case=end

# @lcpr case=start
# [[-1,-1],[-1,3]]\n
# @lcpr case=end

#

