#
# @lc app=leetcode id=36 lang=python3
# @lcpr version=30204
#
# [36] Valid Sudoku
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 检查每一行
        for i in range(9):
            if not self.isValidRow(board[i]):
                return False
            # 检查每一列
            if not self.isValidColumn(board, i):
                return False
            # 检查每个3x3子数独
            if not self.isValidSubBox(board, i // 3 * 3, i % 3 * 3):
                return False
        return True

    def isValidRow(self, row: List[str]) -> bool:
        return self.isValidUnit(row)

    def isValidColumn(self, board: List[List[str]], col: int) -> bool:
        return self.isValidUnit([board[i][col] for i in range(9)])

    def isValidSubBox(self, board: List[List[str]], start_row: int, start_col: int) -> bool:
        return self.isValidUnit([board[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)])

    def isValidUnit(self, unit: List[str]) -> bool:
        unit = [i for i in unit if i != '.']
        return len(unit) == len(set(unit))
        
# @lc code=end



#
# @lcpr case=start
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

# @lcpr case=start
# [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]\n
# @lcpr case=end

#

