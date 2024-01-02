#
# @lc app=leetcode id=2610 lang=python3
#
# [2610] Convert an Array Into a 2D Array With Conditions
#

# @lc code=start
from collections import Counter
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        lines = []
        while counter:
            line = [key for key in counter]
            lines.append(line)
            # print(line)
            for key in line:
                counter[key] -= 1
                if counter[key]==0:
                    del counter[key]
        return lines
# @lc code=end

print(Solution().findMatrix(nums = [1,3,4,1,2,3,1]))
