#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        print(n)
        if n == 1:return True
        if n<0 or n==0 or n%2!=0:return False
        return self.isPowerOfTwo(n//2)
    
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not (n & n - 1)
    
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n.bit_count() == 1
        
# @lc code=end

print(Solution().isPowerOfTwo(16))
print(Solution().isPowerOfTwo(-16))

