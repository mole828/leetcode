#
# @lc app=leetcode id=1759 lang=python3
#
# [1759] Count Number of Homogenous Substrings
#

# @lc code=start
class Solution:
    def countHomogenous(self, s: str) -> int:
        prev = 'X'
        count = 0
        ans = 0
        for c in s:
            if c != prev:
                ans += count*(count+1)//2
                count = 0
            count+=1
            prev = c
        ans += count*(count+1)//2 
        return ans % (10**9+7)
        
# @lc code=end

