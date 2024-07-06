#
# @lc app=leetcode id=2582 lang=python3
# @lcpr version=
#
# [2582] Pass the Pillow
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        ha = [i for i in range(1,n)] + [i for i in range(n,1,-1)]
        # print(ha)
        return ha[time%len(ha)]
# @lc code=end

print(Solution().passThePillow(4,5))

#
# @lcpr case=start
# 4\n5\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n
# @lcpr case=end

#

