#
# @lc app=leetcode id=2966 lang=python3
#
# [2966] Divide Array Into Arrays With Max Difference
#

# @lc code=start
from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        answer:List[List[int]] = []
        box = []
        while nums:
            i = nums.pop() 
            box.append(i)
            if len(box) == 3:
                if box[0] - box[2] > k:
                    return []
                answer.append(box)
                box = [] 
        return answer
# @lc code=end

# 烂题