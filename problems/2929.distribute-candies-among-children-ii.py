#
# @lc app=leetcode id=2929 lang=python3
# @lcpr version=30204
#
# [2929] Distribute Candies Among Children II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def dfs(last_person: int, last_candy: int) -> int:
            if last_person == 0:
                return 1 if last_candy == 0 else 0
            if last_candy == 0:
                return 1
            ans = 0
            for i in range(0, min(last_candy, limit) + 1):
                ans += dfs(last_person - 1, last_candy - i)
            return ans
        return dfs(3, n)
    
class Solution(object):
    def distributeCandies(self, n: int, limit: int) -> int:
        def f(m: int):
            if m < 0:
                return 0
            return (m + 2) * (m + 1) // 2
        
        total = f(n)
        one_exceed = 3 * f(n - limit - 1)
        two_exceed = 3 * f(n - 2 * limit - 2)
        three_exceed = f(n - 3 * limit - 3)
        
        return total - one_exceed + two_exceed - three_exceed
# @lc code=end

print(Solution().distributeCandies(5, 2))

#
# @lcpr case=start
# 5\n2\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n
# @lcpr case=end

#

