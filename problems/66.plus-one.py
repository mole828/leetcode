#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(c) for c in str(int(''.join([str(i) for i in digits]))+1)]
# @lc code=end

if __name__ == '__main__':
    print(Solution().plusOne([2,0,2,6]))

