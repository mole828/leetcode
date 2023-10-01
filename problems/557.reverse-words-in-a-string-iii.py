#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, line: str) -> str:
        return ' '.join(word[::-1] for word in line.split())
# @lc code=end
print(Solution().reverseWords("hello world"))

print([i for i in reversed(['a','b'])])