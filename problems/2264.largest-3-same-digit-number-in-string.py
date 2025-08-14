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
    
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        last_char = 'a'
        count = 1
        res = ""
        for char in num:
            if char == last_char:
                count += 1
            else:
                if count >= 3:
                    res = max(res, last_char * 3)
                last_char = char
                count = 1
            # print(char, count)
        if count >= 3:
            res = max(res, last_char * 3)
        return res

# @lc code=end

# print(Solution().largestGoodInteger("6777133339"))
print(Solution().largestGoodInteger("2213"))
