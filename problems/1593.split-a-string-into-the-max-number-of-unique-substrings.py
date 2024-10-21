#
# @lc app=leetcode id=1593 lang=python3
# @lcpr version=
#
# [1593] Split a String Into the Max Number of Unique Substrings
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(i, has: set[str]):
            if i == len(s):
                return len(has)
            ans = 0
            for j in range(i+1, len(s)+1):
                if s[i:j] not in has:
                    ans = max(ans, dfs(j, has | {s[i:j]}))
            return ans
        return dfs(0, set())
# @lc code=end



#
# @lcpr case=start
# "ababccc"\n
# @lcpr case=end

# @lcpr case=start
# "aba"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n
# @lcpr case=end

#

