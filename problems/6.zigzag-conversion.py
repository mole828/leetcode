#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s 
        pack = numRows * 2 - 2
        rows = [''] * numRows
        for i,c in enumerate(s):
            i = i%pack
            if i>=numRows:
                i = - (i - numRows +2)
            rows[i] += c 
        return ''.join(rows)
          
# @lc code=end

print(Solution().convert("PAYPALISHIRING", 4))
print(Solution().convert("PAYPALISHIRING", 3))