#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
from typing import List

class Solution:
    def candy(self, ratings: List[int], less:int = 1) -> int:
        length = len(ratings)
        gives = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i-1]:
                gives[i] = gives[i-1] + 1
        for i in range(length-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                gives[i] = max(gives[i], gives[i+1]+1)
        return sum(gives)
# @lc code=end

if __name__ == '__main__':
    print(Solution().candy([1,0,2]))