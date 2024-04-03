#
# @lc app=leetcode id=79 lang=python3
# @lcpr version=
#
# [79] Word Search
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import reduce
from typing import List

# Your runtime beats 89.22 % of python3 submissions
# 这都能算是高效率吗？
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool: 
        word_chars = set(word) 
        board_chars = reduce(lambda a,b:a | b,[set(row) for row in board])
        # print(word_chars,board_chars, word_chars-board_chars)
        if len(word_chars-board_chars):
            return False
        
        def next_points(yx: tuple[int,int])->list[tuple[int,int]]:
            y,x = yx
            points:list[tuple[int,int]] = []
            for (dy,dx) in [(-1,0),(1,0),(0,-1),(0,1)]:
                ty = max(0,min(y+dy, len(board)-1))
                tx = max(0,min(x+dx, len(board[0])-1))
                points.append((ty,tx))
            if (y,x) in points:
                points.remove((y,x))
            return points

        def dfs(arrival:List[tuple[int,int]], last_char: str) -> bool:
            # print(f"dfs({arrival},{last_char})")
            if len(last_char) == 0:
                return True 
            for point in next_points(arrival[-1]):
                if point in arrival:
                    continue
                y,x = point
                if board[y][x]==last_char[0]:
                    if dfs(arrival+[point], last_char[1:]):
                        return True
            return False
        
        for y,row in enumerate(board):
            for x,char in enumerate(row):
                if char == word[0] :
                    if dfs([(y,x)], word[1:]):
                        return True
        return False
        
# @lc code=end

print(Solution().exist(
    [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
    "ABCCED"
))

#
# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"SEE"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCB"\n
# @lcpr case=end

#

