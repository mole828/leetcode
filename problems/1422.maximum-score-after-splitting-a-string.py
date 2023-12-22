#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = s.count('1')
        output = 0
        for c in s[:-1]:
            if c is '0':
                left += 1
            else:
                right -= 1
            output = max(output, left+right)
        return output
# @lc code=end

