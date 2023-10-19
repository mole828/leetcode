#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def f(line: str):
            ans = []
            for c in line:
                if c == '#':
                    if ans:
                        ans.pop()
                else:
                    ans.append(c)
            return ''.join(ans)
        return f(s) == f(t)
# @lc code=end

