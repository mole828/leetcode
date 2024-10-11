#
# @lc app=leetcode id=1942 lang=python3
# @lcpr version=
#
# [1942] The Number of the Smallest Unoccupied Chair
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
import heapq
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chars = [0] * len(times)
        heap = []
        ti = sorted((a,b,i) for i,(a,b) in enumerate(times))
        for a,b,i in ti:
            while heap and heap[0][0] <= a:
                _,j = heapq.heappop(heap)
                chars[j] = 0
            for char_i in range(len(chars)):
                if chars[char_i] == 0:
                    chars[char_i] = 1
                    heapq.heappush(heap, (b,char_i))
                    break
            if i == targetFriend:
                return char_i
        return -1

        
# @lc code=end



#
# @lcpr case=start
# [[1,4],[2,3],[4,6]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[3,10],[1,5],[2,6]]\n0\n
# @lcpr case=end

#

