#
# @lc app=leetcode id=1460 lang=python3
# @lcpr version=
#
# [1460] Make Two Arrays Equal by Reversing Subarrays
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n[2,4,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [7]\n[7]\n
# @lcpr case=end

# @lcpr case=start
# [3,7,9]\n[3,7,11]\n
# @lcpr case=end

#

