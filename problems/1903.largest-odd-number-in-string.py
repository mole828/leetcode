#
# @lc app=leetcode id=1903 lang=python3
#
# [1903] Largest Odd Number in String
#

# @lc code=start
class Solution:
    def largestOddNumber(self, num: str) -> str:
        if int(num[-1])%2==1:
            return num
        for i in range (1,len(num)):
            s = num[-i-1]
            if int(s) % 2 == 1:
                return num[:-i]
            
        return ''
# @lc code=end

