#
# @lc app=leetcode id=1750 lang=python3
#
# [1750] Minimum Length of String After Deleting Similar Ends
#

# @lc code=start
class Solution:
    def minimumLength(self, s: str) -> int:
        while len(s)>1 and s[0]==s[-1]:
            c = s[0]
            while s and s[0] == c:
                s = s[1:]
            while s and s[-1] == c:
                s = s[:-1]
            # print(s)
        # print(s)
        return len(s)
# @lc code=end

print(Solution().minimumLength(s = "aabccabba"))