#
# @lc app=leetcode id=1963 lang=python3
# @lcpr version=
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# link: https://leetcode.cn/problems/minimum-number-of-swaps-to-make-the-string-balanced/solutions/922748/shi-zi-fu-chuan-ping-heng-de-zui-xiao-ji-f7ye/
# 数学归纳法
class Solution:
    def minSwaps(self, s: str) -> int:
        cnt = mincnt = 0
        for ch in s:
            if ch == '[':
                cnt += 1
            else:
                cnt -= 1
                mincnt = min(mincnt, cnt)
        return (-mincnt + 1) // 2
# @lc code=end



#
# @lcpr case=start
# "][]["\n
# @lcpr case=end

# @lcpr case=start
# "]]][[["\n
# @lcpr case=end

# @lcpr case=start
# "[]"\n
# @lcpr case=end

#

