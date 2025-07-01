#
# @lc app=leetcode id=3330 lang=python3
#
# [3330] Find the Original Typed String I
#

# @lc code=start
class Solution:
    def possibleStringCount(self, word: str) -> int:
        last_char = '*'
        ans = 1
        count = 0
        for char in word:
            if char == last_char:
                count += 1
            else:
                last_char = char
                ans += count
                count = 0
        ans += count
        return ans
        
# @lc code=end

print(Solution().possibleStringCount("abbcccc"))