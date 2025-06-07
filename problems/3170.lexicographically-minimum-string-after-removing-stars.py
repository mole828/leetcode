#
# @lc app=leetcode id=3170 lang=python3
# @lcpr version=30204
#
# [3170] Lexicographically Minimum String After Removing Stars
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        que = []
        heapq.heapify(que)
        for i,v in enumerate(s):
            if v == '*':
                if que:
                    heapq.heappop(que)
            else:
                heapq.heappush(que, (v, -i))
        return ''.join(v for _,v in sorted((-i,v) for v,i in que))
# @lc code=end



#
# @lcpr case=start
# "aaba*"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

#

