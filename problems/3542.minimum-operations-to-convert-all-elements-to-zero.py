#
# @lc app=leetcode id=3542 lang=python3
#
# [3542] Minimum Operations to Convert All Elements to Zero
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        st = []
        for x in nums:
            while st and x < st[-1]:
                st.pop()
                ans += 1
            if not st or x != st[-1]:
                st.append(x)
        return ans + len(st) - (st[0] == 0)

# @lc code=end

