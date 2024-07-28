#
# @lc app=leetcode id=2976 lang=python3
# @lcpr version=
#
# [2976] Minimum Cost to Convert String I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

import numpy as np


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        mat = np.full((26, 26), np.inf)
        np.fill_diagonal(mat, 0)
        def n(s:str):
            return ord(s)-ord('a')
        for a,b,_cost in zip(original, changed, cost):
            mat[n(a)][n(b)] = min(_cost, mat[n(a)][n(b)])
        for k in range(26):
            mat = np.minimum(mat, mat[:,k,None] + mat[None,k,:])
        result = sum(mat[n(a)][n(b)] for a,b in zip(source,target))
        return -1 if result==np.inf else int(result)

# @lc code=end

print(Solution().minimumCost("abcd", "acbe",["a","b","c","c","e","d"],["b","c","b","e","b","e"],[2,5,5,1,2,20]))

#
# @lcpr case=start
# "abcd"\n"acbe"\n["a","b","c","c","e","d"]\n["b","c","b","e","b","e"]\n[2,5,5,1,2,20]\n
# @lcpr case=end

# @lcpr case=start
# "aaaa"\n"bbbb"\n["a","c"]\n["c","b"]\n[1,2]\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"abce"\n["a"]\n["e"]\n[10000]\n
# @lcpr case=end

#

