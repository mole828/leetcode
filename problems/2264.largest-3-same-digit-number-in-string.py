#
# @lc app=leetcode id=2264 lang=python3
#
# [2264] Largest 3-Same-Digit Number in String
#

# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res=""

        l=0
        r=2

        while r<len(num):
            
            if num[l]==num[r] and num[l]==num[r-1]:
                res=res if res>num[l:r+1] else num[l:r+1]
            
            l+=1
            r+=1
            
        return res
# @lc code=end

