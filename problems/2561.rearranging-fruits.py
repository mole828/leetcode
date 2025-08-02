#
# @lc app=leetcode id=2561 lang=python3
# @lcpr version=30204
#
# [2561] Rearranging Fruits
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter, defaultdict
import heapq
from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count_1 = Counter(basket1)
        count_2 = Counter(basket2)
        count_all = count_1 + count_2
        if any(v%2 for v in count_all.values()):
            return -1
        min_double_cost = min(count_all.keys()) * 2
        should = count_all.copy()
        for k in should:
            should[k] //= 2
        # should = count/2
        print(should)
        swap = (should - count_1) + (should - count_2)
        print(swap)
        arr = sorted(k for k,c in swap.items() for _ in range(c))
        half_arr = arr[:len(arr)//2]
        print(arr, half_arr)
        return sum(
            v if v < min_double_cost else min_double_cost 
            for v in half_arr
        )

# @lc code=end

# print(Solution().minCost(basket1 = [4,2,2,2], basket2 = [1,4,1,2]))
print(Solution().minCost(
    [84,80,43,8,80,88,43,14,100,88],
    [32,32,42,68,68,100,42,84,14,8]
))

#
# @lcpr case=start
# [4,2,2,2]\n[1,4,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4,1]\n[3,2,5,1]\n
# @lcpr case=end

#

