#
# @lc app=leetcode id=2054 lang=python3
# @lcpr version=30204
#
# [2054] Two Best Non-Overlapping Events
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        points = []
        for start, end, value in events:
            points.append((start, 0, value))
            points.append((end, 1, value))

        points.sort()
        max_value = 0
        ans = 0
        for _, status, value in points:
            if status == 0:
                ans = max(ans, max_value + value)
            else:
                max_value = max(max_value, value)

        return ans
        
# @lc code=end

print(Solution().maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]))

#
# @lcpr case=start
# [[1,3,2],[4,5,2],[2,4,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,2],[4,5,2],[1,5,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,5,3],[1,5,1],[6,6,5]]\n
# @lcpr case=end

#

