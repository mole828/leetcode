#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)

        @cache
        def good(numStr: str):
            num = int(numStr)
            return numStr == str(num) and 1<=num<=26
        @cache
        def dp(begin: int) -> int:
            print(f"dp({begin})")
            if begin == length:
                return 1
            back = 0
            if begin+1<=length:
                if good(s[begin:begin+1]):
                    back += dp(begin+1)
            if begin+2<=length:
                if good(s[begin:begin+2]):
                    back += dp(begin+2)
            return back
        
        return dp(0)
# @lc code=end

print(Solution().numDecodings("12"))
