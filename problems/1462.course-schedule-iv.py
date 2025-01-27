#
# @lc app=leetcode id=1462 lang=python3
# @lcpr version=30204
#
# [1462] Course Schedule IV
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        mat = [[float('inf')] * numCourses for _ in range(numCourses)]
        for i in range(numCourses):
            mat[i][i] = 0
        for a, b in prerequisites:
            mat[a][b] = 1
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
        return [mat[a][b] != float('inf') for a, b in queries]
        
# @lc code=end



#
# @lcpr case=start
# 2\n[[1,0]]\n[[0,1],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[]\n[[1,0],[0,1]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[1,2],[1,0],[2,0]]\n[[1,0],[1,2]]\n
# @lcpr case=end

#

