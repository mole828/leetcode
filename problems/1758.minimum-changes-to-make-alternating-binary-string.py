#
# @lc app=leetcode id=1758 lang=python3
#
# [1758] Minimum Changes To Make Alternating Binary String
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        diff = [0, 0]
        for c in s:
            num = int(c)
            diff[num]+=1
            diff.reverse()
        return min(diff)
# @lc code=end

