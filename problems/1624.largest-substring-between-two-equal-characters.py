#
# @lc app=leetcode id=1624 lang=python3
#
# [1624] Largest Substring Between Two Equal Characters
#

# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first: dict[str, int] = {}
        output = -1
        for i,c in enumerate(s):
            if c in first:
                output = max(output, i - first[c] - 1)
            else:
                first[c] = i 
        return output
# @lc code=end

