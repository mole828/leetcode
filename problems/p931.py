from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        matrix.reverse()
        for y in range(1, len(matrix)):
            ty = y-1
            for x in range(len(matrix[y])):
                matrix[y][x] += min(
                    matrix[ty][min(max(0,x+dx),len(matrix)-1)] for dx in [-1,0,1]
                )
        return min(matrix[-1])

if __name__ == '__main__':
    Solution().minFallingPathSum(
        [
            [2,1,3],
            [6,5,4],
            [7,8,9] 
        ]
    )

