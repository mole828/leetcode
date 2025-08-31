#
# @lc app=leetcode id=37 lang=python3
# @lcpr version=30204
#
# [37] Sudoku Solver
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from string import digits
from typing import List, Optional


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_passable: List[List[set[str]]] = [
            [set('123456789') for _ in range(9)] for _ in range(9)
        ]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    board_passable[i][j] = {board[i][j]}
        def hand_row(i: int, v: str):
            for j in range(9):
                board_passable[i][j] -= {v}
        def hand_col(j: int, v: str):
            for i in range(9):
                board_passable[i][j] -= {v}
        def hand_block(i: int, j: int, v: str):
            for k in range(9):
                target_i = i // 3 * 3 + k // 3
                target_j = j // 3 * 3 + k % 3
                print(f"{(i,j)}->{(target_i,target_j)}")
                board_passable[target_i][target_j] -= {v}
        
        while any(any(row) for row in board_passable):
            for i in range(9):
                for j in range(9):
                    value_set = board_passable[i][j]
                    if len(value_set) == 1:
                        v = value_set.pop()
                        board[i][j] = v
                        hand_row(i, v)
                        hand_col(j, v)
                        hand_block(i, j, v)
            # print([any(row) for row in board_passable])


from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board)

    def backtrack(self, board: List[List[str]]) -> bool:
        # 遍历棋盘，寻找一个空格子
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    # 找到空格子，开始尝试填入数字
                    for num_char in "123456789":
                        if self.is_valid(board, i, j, num_char):
                            # 如果这个数字有效，就填入
                            board[i][j] = num_char
                            
                            # 递归地去解决下一个空格子
                            if self.backtrack(board):
                                return True  # 如果找到了解，直接返回 True
                            
                            # 如果基于当前选择无法找到解，就撤销选择（回溯）
                            board[i][j] = '.'
                    
                    # 如果 '1' 到 '9' 都试过了还是无解，说明之前的步骤错了
                    return False
        
        # 如果遍历完整个棋盘都没有找到空格子，说明数独已经解完
        return True

    def is_valid(self, board: List[List[str]], row: int, col: int, num_char: str) -> bool:
        # 检查行
        for j in range(9):
            if board[row][j] == num_char:
                return False
        
        # 检查列
        for i in range(9):
            if board[i][col] == num_char:
                return False
        
        # 检查 3x3 九宫格
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num_char:
                    return False
                    
        return True
    
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_set: List[set[int]] = [set() for _ in range(9)]  # 每行填入的数字
        col_set: List[set[int]] = [set() for _ in range(9)]  # 每列填入的数字
        sub_box_set: List[List[set[int]]] = [[set() for _ in range(3)] for _ in range(3)]  # 每宫填入的数字
        empty_pos = []  # 空格子的位置

        for i, row in enumerate(board):
            for j, b in enumerate(row):
                if b == '.':
                    empty_pos.append((i, j))  # 记录空格子的位置
                else:
                    x = int(b)
                    # 标记行、列、宫包含数字 x
                    row_set[i].add(x)
                    col_set[j].add(x)
                    sub_box_set[i // 3][j // 3].add(x)

        # get_candidates(i, j) 计算 (i, j) 这个空格子的待定数字个数，最小的在堆顶
        get_candidates = lambda i, j: 9 - len(row_set[i] | col_set[j] | sub_box_set[i // 3][j // 3])
        empty_heap = [(get_candidates(i, j), i, j) for i, j in empty_pos]
        heapq.heapify(empty_heap)

        # 每次递归，选一个空格子，枚举填入的数字
        def dfs() -> bool:
            if not empty_heap:  # 所有格子都已填入数字
                return True  # 完成数独

            # 数独玩法：优先考虑待定数字个数最少的空格子
            _, i, j = heapq.heappop(empty_heap)

            candidates = 0  # 受之前填入的数字影响，实际待定数字个数可能比入堆时的少，需要重新计算
            # 枚举 1~9 中没填过的数字 x，填入 board[i][j]
            for x in range(1, 10):
                if x in row_set[i] or x in col_set[j] or x in sub_box_set[i // 3][j // 3]:
                    continue  # x 填过了

                # 把数字 x 转成字符，填入 board[i][j]
                board[i][j] = digits[x]
                # 标记行、列、宫包含数字 x
                
                row_set[i].add(x)
                col_set[j].add(x)
                sub_box_set[i // 3][j // 3].add(x)

                # 填下一个空格子
                if dfs():
                    return True  # 完成数独

                # 恢复现场（撤销）
                # 注意 board[i][j] 无需恢复现场，因为我们会直接覆盖掉之前填入的数字
                row_set[i].remove(x)
                col_set[j].remove(x)
                sub_box_set[i // 3][j // 3].remove(x)

                # 统计待定数字个数
                candidates += 1

            # 恢复现场（撤销）
            heapq.heappush(empty_heap, (candidates, i, j))  # 重新入堆（更新待定数字个数）
            # 所有填法都不行，说明之前（祖先节点）的填法是错的
            return False

        dfs()

# @lc code=end

board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
Solution().solveSudoku(board)
print(board)

#
# @lcpr case=start
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#

