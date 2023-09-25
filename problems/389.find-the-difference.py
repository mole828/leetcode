#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs = Counter(s)
        ct = Counter(t)
        return (ct - cs).popitem()[0]
# @lc code=end
Solution().findTheDifference('ab','abc')
