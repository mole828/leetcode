#
# @lc app=leetcode id=1717 lang=python3
# @lcpr version=
#
# [1717] Maximum Score From Removing Substrings
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# 2025-07-23 day 2

class Solution:
    def maximumGain(self, s: str, x: int, y: int):
        if x < y:
            x, y, s = y, x, s[::-1]
        a = b = ans = 0
        # a 抽象栈
        for c in s:
            if c == 'a':
                a += 1
            elif c == 'b':
                if a:
                    ans += x
                    a -= 1
                else:
                    b += 1
            else:
                ans += min(a,b)*y
                a = b = 0
        return ans + min(a,b)*y

# @lc code=end

print(Solution().maximumGain(s = "cdbcbbaaabab", x = 4, y = 5))

#
# @lcpr case=start
# "cdbcbbaaabab"\n4\n5\n
# @lcpr case=end

# @lcpr case=start
# "aabbaaxybbaabb"\n5\n4\n
# @lcpr case=end

#

