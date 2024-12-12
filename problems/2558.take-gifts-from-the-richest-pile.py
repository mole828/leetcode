#
# @lc app=leetcode id=2558 lang=python3
# @lcpr version=
#
# [2558] Take Gifts From the Richest Pile
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from math import floor
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)
        while k :
            gift = - heapq.heappop(gifts)
            # print(gift)
            gift = floor(gift ** 0.5)
            heapq.heappush(gifts, -gift)
            k -= 1
        return -sum(gifts)

# @lc code=end

print(Solution().pickGifts([25, 64, 9, 4, 100], 4))
print(Solution().pickGifts([1,1,1,1], 4))

#
# @lcpr case=start
# [25,64,9,4,100]\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n4\n
# @lcpr case=end

#

