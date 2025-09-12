#
# @lc app=leetcode id=3227 lang=python3
#
# [3227] Vowels Game in a String
#

# @lc code=start

from functools import cache


VOWELS = set('aeiou')
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        values = [c in VOWELS for c in s]
        # print(values)
        @cache
        def dfs(left: int, alice: int) -> bool:
            vowels_cnt = 0
            for right in range(left, len(values)):
                if values[right]:
                    vowels_cnt += 1
                if vowels_cnt and vowels_cnt % 2 == alice:
                    if not dfs(right+1, 1-alice):
                        return True
            return False
        return dfs(0, 1)

    def doesAliceWin(self, s: str) -> bool:
        return any(c in VOWELS for c in s)
# @lc code=end

print(Solution().doesAliceWin('leetcoder'))
print(Solution().doesAliceWin('bbcd'))
