#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        __start = 0
        for c in s:
            i = t.find(c, __start)
            print(c, i, __start)
            if i == -1:
                return False
            __start = i + 1
        return True
            
# @lc code=end

