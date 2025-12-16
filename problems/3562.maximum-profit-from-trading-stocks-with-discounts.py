#
# @lc app=leetcode id=3562 lang=python3
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#

# @lc code=start
from collections import defaultdict
from math import floor
from typing import Dict, List


fmax = lambda a, b: b if b > a else a

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g = [[] for _ in range(n)]
        for x, y in hierarchy:
            g[x - 1].append(y - 1)

        def dfs(x: int) -> List[Dict[int, int]]:
            sub_f = [defaultdict(int) for _ in range(2)]
            sub_f[0][0] = sub_f[1][0] = 0
            for y in g[x]:
                fy = dfs(y)
                for k, fyk in enumerate(fy):
                    nf = defaultdict(int)
                    for j, pre_res_y in sub_f[k].items():
                        for jy, res_y in fyk.items():
                            sj = j + jy
                            if sj <= budget:
                                nf[sj] = fmax(nf[sj], pre_res_y + res_y)
                    sub_f[k] = nf

            f: List[Dict[int, int]] = [None] * 2
            for k in range(2):
                res = sub_f[0].copy()
                cost = present[x] // (k + 1)
                if cost <= budget:
                    earn = future[x] - cost
                    for j, res_y in sub_f[1].items():
                        sj = j + cost
                        if sj <= budget:
                            res[sj] = fmax(res[sj], res_y + earn)
                f[k] = res
            return f

        return max(dfs(0)[0].values())

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-profit-from-trading-stocks-with-discounts/solutions/3685504/shu-shang-bei-bao-zhuang-tai-ji-dppython-2q7b/
      
# @lc code=end

