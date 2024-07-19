#
# @lc app=leetcode id=1380 lang=python3
# @lcpr version=
#
# [1380] Lucky Numbers in a Matrix
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min_mat = []
        for row in matrix:
            row_min = min(row)
            row_min_mat.append([x==row_min for x in row])
        col_max_mat = []
        for x in range(len(matrix[0])):
            col_max = max(matrix[y][x] for y in range(len(matrix)))
            col_max_mat.append([matrix[y][x]==col_max for y in range(len(matrix))])
        print(row_min_mat, col_max_mat)
        ans = []
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if row_min_mat[y][x] and col_max_mat[x][y]:
                    ans.append(matrix[y][x])
        return ans

# @lc code=end

print(Solution().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))

#
# @lcpr case=start
# [[3,7,8],[9,11,13],[15,16,17]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,10,4,2],[9,3,8,7],[15,16,17,12]]\n
# @lcpr case=end

# @lcpr case=start
# [[7,8],[1,2]]\n
# @lcpr case=end

#

