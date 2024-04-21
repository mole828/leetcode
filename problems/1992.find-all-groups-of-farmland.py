#
# @lc app=leetcode id=1992 lang=python3
# @lcpr version=
#
# [1992] Find All Groups of Farmland
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows = len(land)
        cols = len(land[0])
        has_check = [[0]*cols for _ in range(rows)]
        lands = []
        for top in range(rows):
            for left in range(cols):
                if has_check[top][left]:
                    continue
                if land[top][left]:
                    right = left
                    while right<cols and land[top][right]:
                        right += 1
                    right -= 1
                    bottom = top 
                    while bottom<rows and all(land[bottom][left:right+1]):
                        for col in range(left,right+1):
                            has_check[bottom][col] = 1
                        bottom += 1
                    bottom -= 1
                    lands.append([top,left,bottom,right])
        return lands
# @lc code=end



#
# @lcpr case=start
# [[1,0,0],[0,1,1],[0,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0]]\n
# @lcpr case=end

#

