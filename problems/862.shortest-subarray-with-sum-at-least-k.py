#
# @lc app=leetcode id=862 lang=python3
# @lcpr version=30204
#
# [862] Shortest Subarray with Sum at Least K
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        result = []
        for left in range(len(nums)):
            for right in range(left, len(nums)):
                arr = nums[left : right + 1]
                if sum(arr) >= k:
                    result.append(len(arr))

        if result:
            return min(result)
        else:
            return -1

   
from numpy import inf
from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = inf
        c_s = 0
        q = deque()
        q.append((-1,0))
        for i, x in enumerate(nums):
            c_s += x
            # in
            while q and q[-1][1] >= c_s:
                q.pop()
            q.append((i, c_s))
            # out
            while q and c_s - q[0][1] >= k:
                ans = min(ans, i - q.popleft()[0])
        return ans if ans < inf else -1


            
# @lc code=end



#
# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n4\n
# @lcpr case=end

# @lcpr case=start
# [2,-1,2]\n3\n
# @lcpr case=end

#

