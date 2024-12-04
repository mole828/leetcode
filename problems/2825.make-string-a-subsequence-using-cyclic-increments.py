#
# @lc app=leetcode id=2825 lang=python3
# @lcpr version=
#
# [2825] Make String a Subsequence Using Cyclic Increments
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
oa = ord('a')
class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        if len(s) < len(t):
            return False
        j = 0
        for b in s:
            c = chr((ord(b) + 1 - oa)%26 + oa)
            if b == t[j] or c == t[j]:
                j += 1
                if j == len(t):
                    return True
        return False
# @lc code=end



#
# @lcpr case=start
# "abc"\n"ad"\n
# @lcpr case=end

# @lcpr case=start
# "zc"\n"ad"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"d"\n
# @lcpr case=end

#

