#
# @lc app=leetcode id=869 lang=python3
# @lcpr version=30204
#
# [869] Reordered Power of 2
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n = sorted(list(str(n)))
        for i in range(30):
            if n == sorted(list(str(2**i))):
                return True
        return False
# @lc code=end



#
# @lcpr case=start
# 1\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#

