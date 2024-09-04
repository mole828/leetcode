#
# @lc app=leetcode id=1945 lang=python3
# @lcpr version=
#
# [1945] Sum of Digits of String After Convert
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ''.join(str(ord(c)-ord("a")+1)for c in s)
        while k:
            res = sum(int(c) for c in str(res))
            k -= 1
        return res
# @lc code=end

print(Solution().getLucky("leetcode", 2))

#
# @lcpr case=start
# "iiii"\n1\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n2\n
# @lcpr case=end

# @lcpr case=start
# "zbax"\n2\n
# @lcpr case=end

#

