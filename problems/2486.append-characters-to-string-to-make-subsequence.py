#
# @lc app=leetcode id=2486 lang=python3
# @lcpr version=
#
# [2486] Append Characters to String to Make Subsequence
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        arr_s, arr_t = list(s), list(t)
        while arr_s and arr_t:
            c = arr_s.pop(0)
            if c == arr_t[0]:
                arr_t.pop(0)
        return len(arr_t)
# @lc code=end



#
# @lcpr case=start
# "coaching"\n"coding"\n
# @lcpr case=end

# @lcpr case=start
# "abcde"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "z"\n"abcde"\n
# @lcpr case=end

#

