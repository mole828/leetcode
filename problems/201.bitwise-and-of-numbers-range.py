#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
from functools import reduce

# Timeout, Of course
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        return reduce(lambda a,b:a & b, range(left, right+1))
    

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int: 
        ans = 1 
        while ans < right:
            ans <<= 1 
            ans += 1
        for num in range(left, right+1):
            ans &= num 
            # print(ans, num)
            if ans == 0:
                break
        return ans 
    

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt

# @lc code=end

print(Solution().rangeBitwiseAnd(left = 1, right = 2147483647))
print(Solution().rangeBitwiseAnd(left = 5, right = 7))