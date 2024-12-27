#
# @lc app=leetcode id=1014 lang=python3
# @lcpr version=
#
# [1014] Best Sightseeing Pair
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


# 链接：https://leetcode.cn/problems/best-sightseeing-pair/solutions/2836414/mei-ju-you-wei-hu-zuo-jian-ji-xie-fa-pyt-x385/
# 数学公式分解
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = mx = 0  # mx 表示 j 左边的 values[i] + i 的最大值
        for j, v in enumerate(values):
            ans = max(ans, mx + v - j)
            mx = max(mx, v + j)
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [8,1,5,2,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

