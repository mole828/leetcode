#
# @lc app=leetcode id=1310 lang=python3
# @lcpr version=
#
# [1310] XOR Queries of a Subarray
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        mp = {}
        curr = 0
        for i, v in enumerate(arr):
            curr ^= v
            mp[i] = curr

        res = []

        for l, r in queries:
            if l == 0:
                res.append(mp[r])

            else:
                res.append(mp[l-1] ^ mp[r])

        return res
# @lc code=end



#
# @lcpr case=start
# [1,3,4,8]\n[[0,1],[1,2],[0,3],[3,3]]\n
# @lcpr case=end

# @lcpr case=start
# [4,8,2,10]\n[[2,3],[1,3],[0,0],[0,3]]\n
# @lcpr case=end

#

