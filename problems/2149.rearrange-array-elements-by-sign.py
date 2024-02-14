#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [] 
        nag = [] 
        for num in nums:
            if num < 0:
                nag.append(num)
            else:
                pos.append(num)
        output = [] 
        arrs = [pos, nag]
        # print(arrs)
        while arrs[0]:
            output.append(arrs[0].pop(0))
            arrs.reverse()
        return output
# @lc code=end

print(Solution().rearrangeArray([3,1,-2,-5,2,-4]))