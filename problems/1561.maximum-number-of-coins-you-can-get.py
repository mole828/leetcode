#
# @lc app=leetcode id=1561 lang=python3
#
# [1561] Maximum Number of Coins You Can Get
#

# @lc code=start
from typing import List
from collections import deque

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        que = deque(piles)
        ans = 0
        while que:
            que.popleft()
            que.pop()
            # pop use list runtime 5% memory 95%
            # pop use deque runtime 91% memory 6%
            ans += que.pop()
        return ans 
# @lc code=end

print(Solution().maxCoins(piles = [2,4,1,2,7,8]))

print(Solution().maxCoins(piles = [9,8,7,6,5,1,2,3,4]))