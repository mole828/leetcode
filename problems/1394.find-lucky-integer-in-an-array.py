#
# @lc app=leetcode id=1394 lang=python3
# @lcpr version=30204
#
# [1394] Find Lucky Integer in an Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        return max((num for num, count in counter.items() if num == count), default=-1)
# @lc code=end



#
# @lcpr case=start
# [2,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,3,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,3,3]\n
# @lcpr case=end

#

