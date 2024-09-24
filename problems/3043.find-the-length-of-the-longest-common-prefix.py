#
# @lc app=leetcode id=3043 lang=python3
# @lcpr version=
#
# [3043] Find the Length of the Longest Common Prefix
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def f(arr):
            se = set()
            for i, x in enumerate(arr):
                while x and x not in se:
                    se.add(x)
                    x //= 10
            return se
        return len(str(max(f(arr1) & f(arr2), default = "")))
# @lc code=end



#
# @lcpr case=start
# [1,10,100]\n[1000]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n[4,4,4]\n
# @lcpr case=end

#

