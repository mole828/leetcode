#
# @lc app=leetcode id=1061 lang=python3
#
# [1061] Lexicographically Smallest Equivalent String
#

# @lc code=start
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ord_a = ord('a')
        groups = {chr(ord_a+i): set([chr(ord_a + i)]) for i in range(26)}
        for char_1, char_2 in zip(s1,s2):
            union_group = groups[char_1].union(groups[char_2])
            for char in union_group:
                groups[char] = union_group
        
        return ''.join(min(groups[char]) for char in baseStr)
            

# @lc code=end

print(Solution().smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser"))