#
# @lc app=leetcode id=898 lang=python3
#
# [898] Bitwise ORs of Subarrays
#

# @lc code=start
from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        for i, x in enumerate(arr):
            ans.add(x)
            for j in range(i-1, -1, -1):
                if arr[j] | x == arr[j]:
                    break
                arr[j] |= x
                ans.add(arr[j])
        return len(ans)
            
# @lc code=end

