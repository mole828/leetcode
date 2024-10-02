#
# @lc app=leetcode id=1331 lang=python3
# @lcpr version=
#
# [1331] Rank Transform of an Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        rank = {num: i + 1 for i, num in enumerate(sorted_arr)}
        return [rank[num] for num in arr]
        
# @lc code=end



#
# @lcpr case=start
# [40,10,20,30]\n
# @lcpr case=end

# @lcpr case=start
# [100,100,100]\n
# @lcpr case=end

# @lcpr case=start
# [37,12,28,9,100,56,80,5,12]\n
# @lcpr case=end

#

