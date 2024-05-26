#
# @lc app=leetcode id=552 lang=python3
# @lcpr version=
#
# [552] Student Attendance Record II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache


class Solution:
    # Memory Limit Exceeded
    # 36/59 cases passed (N/A)
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        @cache
        def f(last: int, last_a: int, last_l: int) -> int:
            if not last:
                return 1
            total = 0
            total += f(last-1, last_a, 2)
            if last_a:
                total += f(last-1, last_a=last_a-1, last_l=2)
            if last_l:
                total += f(last-1, last_a, last_l=last_l-1)
            return total % MOD
        return f(n, 1, 2)
        
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        last_floor = [[1]*3 for _ in range(2)]
        for i in range(n):
            new_floor = [[0]*3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    new_floor[a][l] += last_floor[a][2]
                    if a:
                        new_floor[a][l] += last_floor[a-1][2]
                    if l:
                        new_floor[a][l] += last_floor[a][l-1]
                    new_floor[a][l] %= MOD
            last_floor = new_floor
        return last_floor[1][2]

# @lc code=end

print(Solution().checkRecord(10101))

#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 10101\n
# @lcpr case=end

#

