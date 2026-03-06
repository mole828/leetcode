#
# @lc app=leetcode id=1784 lang=python3
#
# [1784] Check if Binary String Has at Most One Segment of Ones
#

# @lc code=start
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        cnt = 0
        s += '0'
        iter_s = iter(s)
        last = next(iter_s)
        for c in iter_s:
            if last == '1' and c == '0':
                cnt += 1
            last = c
        return cnt <= 1
# @lc code=end

