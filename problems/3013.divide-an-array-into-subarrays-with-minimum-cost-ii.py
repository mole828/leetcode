#
# @lc app=leetcode id=3013 lang=python3
#
# [3013] Divide an Array Into Subarrays With Minimum Cost II
#

# @lc code=start
import sys
from typing import List
from functools import lru_cache

from sortedcontainers import SortedList

# 提升递归深度限制，防止爆栈
# sys.setrecursionlimit(2000)

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        inf = float('inf')

        @lru_cache(None)
        def solve(idx: int, count: int, limit: int) -> int:
            # 找齐了剩下的 k-1 个数
            if count == 0:
                return 0
            # 越界或超过了窗口限制
            if idx >= n or idx > limit:
                return inf
            
            # 选项 1: 选当前的 nums[idx]
            # 如果这是选的第一个数（count == k-1），则由此确定窗口的 limit
            new_limit = limit
            if count == k - 1:
                new_limit = idx + dist
            
            res_pick = nums[idx] + solve(idx + 1, count - 1, new_limit)
            
            # 选项 2: 不选当前的，看下一个
            res_skip = solve(idx + 1, count, limit)
            
            return min(res_pick, res_skip)

        # nums[0] 必选，从下标 1 开始选剩下的 k-1 个，初始 limit 为无穷大
        return nums[0] + solve(1, k - 1, inf)


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        k -= 1
        sum_left = sum(nums[:dist + 2])
        L = SortedList(nums[1:dist + 2])
        R = SortedList()

        def L2R() -> None:
            x = L.pop()
            nonlocal sum_left
            sum_left -= x
            R.add(x)

        def R2L() -> None:
            x = R.pop(0)
            nonlocal sum_left
            sum_left += x
            L.add(x)

        while len(L) > k:
            L2R()

        ans = sum_left
        for i in range(dist + 2, len(nums)):
            # 移除 out
            out = nums[i - dist - 1]
            if out in L:
                sum_left -= out
                L.remove(out)
            else:
                R.remove(out)

            # 添加 in
            in_val = nums[i]
            if in_val < L[-1]:
                sum_left += in_val
                L.add(in_val)
            else:
                R.add(in_val)

            # 维护大小
            if len(L) == k - 1:
                R2L()
            elif len(L) == k + 1:
                L2R()

            ans = min(ans, sum_left)

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/solutions/2614067/liang-ge-you-xu-ji-he-wei-hu-qian-k-1-xi-zdzx/

# @lc code=end

# 测试代码
if __name__ == "__main__":
    # 样例 1: [1,3,2,6,4,2], k=3, dist=3 -> 结果应为 5 (选 1, 2, 2)
    print(Solution().minimumCost(nums=[1,3,2,6,4,2], k=3, dist=3))
    print(Solution().minimumCost([10, 1, 2, 2, 2, 1], 4, 3))
