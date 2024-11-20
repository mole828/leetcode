#
# @lc app=leetcode id=2516 lang=python3
# @lcpr version=
#
# [2516] Take K of Each Character From Left and Right
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = [0, 0, 0]
        for c in s:
            count[ord(c) - ord('a')] += 1

        if min(count) < k:
            return -1

        res = float("inf")
        l = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord('a')] -= 1

            while min(count) < k:
                count[ord(s[l]) - ord('a')] += 1
                l += 1
            res = min(res, len(s) - (r - l + 1))
        return res
# @lc code=end



#
# @lcpr case=start
# "aabaaaacaabc"\n2\n
# @lcpr case=end

# @lcpr case=start
# "a"\n1\n
# @lcpr case=end

#

