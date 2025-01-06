#
# @lc app=leetcode id=1769 lang=python3
# @lcpr version=
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        for i in range(n):
            for j in range(n):
                if boxes[j] == '1':
                    ans[i] += abs(i - j)
        return ans
# @lc code=end



#
# @lcpr case=start
# "110"\n
# @lcpr case=end

# @lcpr case=start
# "001011"\n
# @lcpr case=end

#

