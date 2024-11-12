#
# @lc app=leetcode id=2070 lang=python3
# @lcpr version=
#
# [2070] Most Beautiful Item for Each Query
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from bisect import bisect_left
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        max_values = []
        max_value = 0
        for i in range(len(items)):
            max_value = max(max_value, items[i][1])
            max_values.append(max_value)
        ans = []
        for q in queries:
            i = bisect_left(items, [q + 1, 0]) - 1
            ans.append(max_values[i] if i >= 0 else 0)
        return ans
# @lc code=end



#
# @lcpr case=start
# [[1,2],[3,2],[2,4],[5,6],[3,5]]\n[1,2,3,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2],[1,2],[1,3],[1,4]]\n[1]\n
# @lcpr case=end

# @lcpr case=start
# [[10,1000]]\n[5]\n
# @lcpr case=end

#

