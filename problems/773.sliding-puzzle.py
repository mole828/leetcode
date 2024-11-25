#
# @lc app=leetcode id=773 lang=python3
# @lcpr version=
#
# [773] Sliding Puzzle
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

import numpy as np
from numpy import ndarray

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        o_board: ndarray[ndarray[int]] = np.array(board)
        target_board = np.array([[1,2,3],[4,5,0]])
        status_set: set[tuple] = set()
        que = [(o_board,0)]
        while que:
            current_board, deep = que.pop(0)
            status = tuple(current_board.flatten())
            if status in status_set:
                continue
            status_set.add(status)
            if np.array_equal(current_board, target_board):
                return deep
            p0 = np.where(current_board == 0)
            for d in [[0,1],[1,0],[-1,0],[0,-1]]:
                p = p0[0] + d[0], p0[1] + d[1]
                if p[0] < 0 or p[0] > 1 or p[1] < 0 or p[1] > 2:
                    continue
                new_board = current_board.copy()
                new_board[p0] = new_board[p]
                new_board[p] = 0
                que.append((new_board, deep + 1))
        return -1



        
# @lc code=end

# print(Solution().slidingPuzzle([[1,2,3],[4,0,5]]))
print(Solution().slidingPuzzle([[4,1,2],[5,0,3]]))

#
# @lcpr case=start
# [[1,2,3],[4,0,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[5,4,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,1,2],[5,0,3]]\n
# @lcpr case=end

#

