from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ans = [[0]*len(colSum) for _ in range(len(rowSum))]
        for r in range(len(rowSum)):
            for c in range(len(colSum)):
                temp = min(rowSum[r],colSum[c])
                ans[r][c] = temp
                rowSum[r] -= temp
                colSum[c] -= temp
        return ans