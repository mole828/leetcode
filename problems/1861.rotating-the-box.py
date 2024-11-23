#
# @lc app=leetcode id=1861 lang=python3
# @lcpr version=
#
# [1861] Rotating the Box
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

import numpy as np
from numpy import ndarray

# Time Limit Exceeded, 85 / 87 testcases passed
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        box:ndarray[ndarray[str]] = np.array(box)
        box = np.rot90(box, -1)
        print(box)
        def fall():
            count = 0
            for y in range(box.shape[0]-1):
                for x in range(box.shape[1]):
                    if box[y][x] == "*":
                        continue
                    if box[y][x] == "#" and box[y+1][x] == ".":
                        box[y][x] = "."
                        box[y+1][x] = "#"
                        count += 1
            return count
        while fall():
            pass
        
        return box.tolist()

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        box:ndarray[ndarray[str]] = np.array(box)
        box = np.rot90(box)
        print(box)
        for y,row in enumerate(box):
            if y == 0:
                continue
            for x,c in enumerate(row):
                if c == "*":
                    continue
                if c == "#" and box[y-1][x] == ".":
                    yy = y
                    while box[yy-1][x] == ".":
                        box[yy-1][x] = "#"
                        box[yy][x] = "."
                        yy -= 1
                        if yy == 0:
                            break
        box = np.rot90(box, -2)
        return box.tolist()

        
        
# @lc code=end

print(Solution().rotateTheBox([["#",".","#"]]))

#
# @lcpr case=start
# [["#",".","#"]]\n
# @lcpr case=end

# @lcpr case=start
# [["#",".","*","."],["#","#","*","."]]\n
# @lcpr case=end

# @lcpr case=start
# [["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]\n
# @lcpr case=end

#

