#
# @lc app=leetcode id=1122 lang=python3
# @lcpr version=
#
# [1122] Relative Sort Array
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index = {v:k for k,v in enumerate(arr2)}
        def get(x:int):
            if x not in index:
                return 1000+x
            return index[x]
        return sorted(arr1, key=get)
# @lc code=end



#
# @lcpr case=start
# [2,3,1,3,2,4,6,7,9,2,19]\n[2,1,4,3,9,6]\n
# @lcpr case=end

# @lcpr case=start
# [28,6,22,8,44,17]\n[22,28,8,6]\n
# @lcpr case=end

#

