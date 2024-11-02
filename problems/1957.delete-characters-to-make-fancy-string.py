#
# @lc app=leetcode id=1957 lang=python3
# @lcpr version=
#
# [1957] Delete Characters to Make Fancy String
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == ans[-1]:
                cnt += 1
                if cnt < 3:
                    ans += s[i]
            else:
                cnt = 1
                ans += s[i]
        return ans
# @lc code=end


