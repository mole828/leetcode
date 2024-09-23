#
# @lc app=leetcode id=2707 lang=python3
# @lcpr version=
#
# [2707] Extra Characters in a String
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
from typing import List

# link https://leetcode.cn/problems/extra-characters-in-a-string/solutions/2286613/dong-tai-gui-hua-cong-ji-yi-hua-sou-suo-wtd7a/
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = set(dictionary)
        @cache
        def dfs(i: int) -> int:
            if i < 0: return 0
            res = dfs(i - 1) + 1  
            for j in range(i + 1): 
                if s[j:i + 1] in d:
                    res = min(res, dfs(j - 1))
            return res
        return dfs(len(s) - 1)

# @lc code=end



#
# @lcpr case=start
# "leetscode"\n["leet","code","leetcode"]\n
# @lcpr case=end

# @lcpr case=start
# "sayhelloworld"\n["hello","world"]\n
# @lcpr case=end

#

