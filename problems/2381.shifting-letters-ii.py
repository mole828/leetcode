#
# @lc app=leetcode id=2381 lang=python3
# @lcpr version=30204
#
# [2381] Shifting Letters II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

import numpy as np

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        oa = ord('a')
        sum_shifts = np.zeros(n, dtype=int)
        for a,b,d in shifts:
            sum_shifts[a:b+1] += 1 if d else -1

        return ''.join([chr((ord(c)-oa+sum_shift)%26+oa) for c,sum_shift in zip(s,sum_shifts)])
        
# @lc code=end



#
# @lcpr case=start
# "abc"\n[[0,1,0],[1,2,1],[0,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# "dztz"\n[[0,0,0],[1,1,1]]\n
# @lcpr case=end

#

