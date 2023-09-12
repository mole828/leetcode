#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        print(n)
        if n is 1:return True
        if n<0 or n==0 or n%2!=0:return False
        return self.isPowerOfTwo(n//2)
        
# @lc code=end

Solution().isPowerOfTwo(16)