#
# @lc app=leetcode id=2570 lang=python3
# @lcpr version=30204
#
# [2570] Merge Two 2D Arrays by Summing Values
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        counter = Counter()
        for index,value in nums1:
            counter[index] += value
        for index,value in nums2:
            counter[index] += value
        sorted_keys = sorted(counter.keys())
        return [[key, counter[key]] for key in sorted_keys]
        
# @lc code=end



#
# @lcpr case=start
# [[1,2],[2,3],[4,5]]\n[[1,4],[3,2],[4,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,4],[3,6],[5,5]]\n[[1,3],[4,3]]\n
# @lcpr case=end

#

