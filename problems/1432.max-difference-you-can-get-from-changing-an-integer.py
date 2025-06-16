#
# @lc app=leetcode id=1432 lang=python3
#
# [1432] Max Difference You Can Get From Changing an Integer
#

# @lc code=start
class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        mx = num
        for d in s:
            if d != '9':
                mx = int(s.replace(d, '9'))
                break

        mn = num
        if s[0] != '1':
            mn = int(s.replace(s[0], '1'))
        else:
            for d in s:
                if d > '1':
                    mn = int(s.replace(d, '0'))
                    break

        return mx - mn

# @lc code=end

print(Solution().maxDiff(555))
print(Solution().maxDiff(9))