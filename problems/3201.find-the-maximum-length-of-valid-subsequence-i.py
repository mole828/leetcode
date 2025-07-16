#
# @lc app=leetcode id=3201 lang=python3
#
# [3201] Find the Maximum Length of Valid Subsequence I
#

# @lc code=start
from typing import List

"""
(a+b) mod k = (b+c) mod k
=> (a+b-(b+c)) mod k = 0
=> (a-c) mod k = 0

k = 2 时
[
    [a, b,]
    [c, d,]
]
x = 2
x_mod_k = x % 2 = 0
mat[0][x_mod_k] = mat[x_mod_k][0] + 1 # a+a mod k = 0
mat[1][x_mod_k] = mat[x_mod_k][1] + 1 # b+c mod k = 0
"""
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        k = 2
        mat = [[0]*k for _ in range(k)]
        for x in nums:
            x_mod_k = x % k
            for y, v in enumerate(mat[x_mod_k]):
                mat[y][x_mod_k] = v + 1
            # print(x, mat)
        return max(map(max, mat))


# @lc code=end

print(Solution().maximumLength([1,2,3,4]))
print(Solution().maximumLength([1,2,1,1,2,1,2]))
print(Solution().maximumLength([1,8,4,2,4]))