from bisect import bisect_left, bisect_right
from itertools import accumulate
from typing import List

'''
TODO
'''

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # 贪心：走的范围最大
        # 先一个方向走x步，再另一个方向k - x步
        pos = [fruit[0] for fruit in fruits]
        val = [fruit[1] for fruit in fruits]
        preSum = list(accumulate(val, initial = 0))
        ans = 0
        # 1.先左走x，再右走k - x
        # [start - x, start + k - 2x]
        for x in range(k + 1):
            i = bisect_left(pos, startPos - x)
            j = bisect_right(pos, startPos + k - 2 * x)
            res1 = preSum[j] - preSum[i]
            # 1.先右走x，再左走k - x
            # [start + 2x - k, start + x]
            i = bisect_left(pos, startPos + 2 * x - k)
            j = bisect_right(pos, startPos + x)
            res2 = preSum[j] - preSum[i]
            ans = max(ans, max(res1, res2))
        # 结果
        return ans


if __name__ == '__main__':
    assert Solution().maxTotalFruits(fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4) == 9
    assert Solution().maxTotalFruits(fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4) == 14