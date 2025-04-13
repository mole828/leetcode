#
# @lc app=leetcode id=1922 lang=python3
# @lcpr version=30204
#
# [1922] Count Good Numbers
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    MOD = 10**9 + 7
    # max deepth of recursion is 1000
    def countGoodNumbers(self, n: int) -> int:
        def dfs(n: int, even: bool) -> int:
            if n == 0:
                return 1
            if even:
                return dfs(n - 1, False) * 5 % self.MOD
            else:
                return dfs(n - 1, True) * 4 % self.MOD
        return dfs(n, True) % self.MOD
    def countGoodNumbers(self, n: int) -> int:
        # n = n % 1000
        b = pow(20,(n//2), self.MOD)
        a = (5**(n%2)) * b % self.MOD
        return a

        
# @lc code=end

print(Solution().countGoodNumbers(1))
print(Solution().countGoodNumbers(4))
print(Solution().countGoodNumbers(50))
print(Solution().countGoodNumbers(1924))

#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 50\n
# @lcpr case=end

#

