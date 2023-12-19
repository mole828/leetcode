#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#

# @lc code=start
from itertools import product
import math
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        nRows = len(img)
        nCols = len(img[0])
        values = [[0]*nCols for row in range(nRows)]
        times = [[0]*nCols for row in range(nRows)]
        for y, row in enumerate(img):
            for x, value in enumerate(row):
                for dy,dx in product([-1,0,1],[-1,0,1]):
                    ty = y + dy 
                    tx = x + dx 
                    if 0 <= ty < nRows and 0 <= tx < nCols:
                        values[ty][tx] += value 
                        times[ty][tx] += 1
        return [
            [value//times[y][x] for x, value in enumerate(row)]
            for y, row in enumerate(values)
        ]
# @lc code=end

