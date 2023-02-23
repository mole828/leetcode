from typing import List


class Solution:
    # 89. 格雷编码 官方题解
    def grayCode(self, n: int) -> List[int]:
        ans = [0] * (1 << n)
        for i in range(1 << n):
            ans[i] = (i >> 1) ^ i
        return ans

    def circularPermutation(self, n: int, start: int) -> List[int]:
        p = self.grayCode(n) * 2
        for i, x in enumerate(p):
            if x == start:
                return p[i:len(p) // 2 + i]