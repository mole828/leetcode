#
# @lc app=leetcode id=2094 lang=python3
#
# [2094] Finding 3-Digit Even Numbers
#

# @lc code=start
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()
        result = set()
        def dfs(i: int, j: int, k: int):
            if i == j or j == k or i == k:
                return
            a, b, c = digits[i], digits[j], digits[k]
            if a == 0:
                return
            if c % 2 != 0:
                return
            num = a * 100 + b * 10 + c 
            result.add(num)
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    dfs(i, j, k)
        return sorted(result)
# @lc code=end

print(Solution().findEvenNumbers(digits = [2,1,3,0]))