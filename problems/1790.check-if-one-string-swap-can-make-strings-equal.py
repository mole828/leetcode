#
# @lc app=leetcode id=1790 lang=python3
# @lcpr version=30204
#
# [1790] Check if One String Swap Can Make Strings Equal
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
        return diff == 0 or diff == 2
# @lc code=end



#
# @lcpr case=start
# "bank"\n"kanb"\n
# @lcpr case=end

# @lcpr case=start
# "attack"\n"defend"\n
# @lcpr case=end

# @lcpr case=start
# "kelb"\n"kelb"\n
# @lcpr case=end

#

