#
# @lc app=leetcode id=624 lang=python3
# @lcpr version=
#
# [624] Maximum Distance in Arrays
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
import numpy as np

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        preMin, preMax = arrays[0][0], arrays[0][len(arrays[0]) - 1]
        ans = -np.inf
        for i in range(1, len(arrays)):
            x, y = arrays[i][0], arrays[i][len(arrays[i]) - 1]
            ans = max(ans, max(preMax - x, y - preMin))
            preMax = max(preMax, y)
            preMin = min(preMin, x)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5],[1,2,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1],[1]]\n
# @lcpr case=end

#

