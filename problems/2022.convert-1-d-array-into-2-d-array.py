#
# @lc app=leetcode id=2022 lang=python3
# @lcpr version=
#
# [2022] Convert 1D Array Into 2D Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        return [original[i * n: (i + 1) * n] for i in range(m)]
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n2\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n1\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n1\n
# @lcpr case=end

#

