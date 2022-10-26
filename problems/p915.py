
from typing import List

import numpy

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        lm = numpy.Infinity
        sm = 0
        index = 0
        for i in range(len(nums)):
            num = nums[i]
            sm = max(sm,num)
            if num < lm:
                lm = sm 
                index = i
        return index + 1

if __name__ == '__main__':
    sol = Solution()
    for data in [
        [5,0,3,8,6], # 3
        [1,1,1,0,6,12], # 4
        [1,1], # 1
    ]:
        print(data, '=>', sol.partitionDisjoint(data))