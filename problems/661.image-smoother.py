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
        values = [[0]*len(img[row]) for row in range(len(img))]
        times = [[0]*len(img[row]) for row in range(len(img))]
        def add(y: int, x: int, value: int):
            if 0 <= y < len(values):
                values_row = values[y]
                times_row = times[y]
                if 0 <= x < len(values_row):
                    values_row[x] += value 
                    times_row[x] += 1
        for y, row in enumerate(img):
            for x, value in enumerate(row):
                for dy,dx in product([-1,0,1],[-1,0,1]):
                    ty = y + dy 
                    tx = x + dx 
                    add(ty, tx, value)
        return [
            [value//times[y][x] for x, value in enumerate(row)]
            for y, row in enumerate(values)
        ]
# @lc code=end

