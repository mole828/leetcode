#
# @lc app=leetcode id=205 lang=python3
# @lcpr version=
#
# [205] Isomorphic Strings
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s,t)))==len(set(s))==len(set(t))
# @lc code=end

print(Solution().isIsomorphic('paper', 'title'))

#
# @lcpr case=start
# "egg"\n"add"\n
# @lcpr case=end

# @lcpr case=start
# "foo"\n"bar"\n
# @lcpr case=end

# @lcpr case=start
# "paper"\n"title"\n
# @lcpr case=end

#

