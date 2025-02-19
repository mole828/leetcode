#
# @lc app=leetcode id=1415 lang=python3
#
# [1415] The k-th Lexicographical String of All Happy Strings of Length n
#

# @lc code=start
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        all_happy_strings = []
        def dfs(i: int, s: str):
            if i == n:
                all_happy_strings.append(s)
                return
            for c in 'abc':
                if not s or s[-1] != c:
                    dfs(i+1, s+c)
        dfs(0, '')
        return all_happy_strings[k-1] if k <= len(all_happy_strings) else ''
# @lc code=end

