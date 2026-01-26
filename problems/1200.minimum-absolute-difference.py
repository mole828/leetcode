#
# @lc app=leetcode id=1200 lang=python3
#
# [1200] Minimum Absolute Difference
#

# @lc code=start
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        result = []
        n = len(arr)
        for i in range(1, n):
            diff = arr[i] - arr[i - 1]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i - 1], arr[i]]]
            elif diff == min_diff:
                result.append([arr[i - 1], arr[i]])
        return result
# @lc code=end

