#
# @lc app=leetcode id=2593 lang=python3
# @lcpr version=
#
# [2593] Find Score of an Array After Marking All Elements
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
import heapq
from typing import List

import numpy as np


inf = 10**7
# Time Limit Exceeded, 1036/1044 cases passed
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        visited = np.array([0] * n)
        ans = 0
        while not visited.all():
            ad = (visited * inf) 
            mat = nums + ad
            min_idx = np.argmin(mat)
            ans += nums[min_idx]
            visited[min_idx] = True
            if min_idx > 0:
                visited[min_idx - 1] = True
            if min_idx < n - 1:
                visited[min_idx + 1] = True
        return ans
    
class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [(num, idx) for idx, num in enumerate(nums)]
        heapq.heapify(heap)
        marked = set()
        ans = 0
        while heap:
            num, idx = heapq.heappop(heap)
            if idx in marked:
                continue
            ans += num
            marked.add(idx)
            marked.add(idx - 1)
            marked.add(idx + 1)
        return ans

# @lc code=end

print(Solution().findScore([2,1,3,4,5,2]))

#
# @lcpr case=start
# [2,1,3,4,5,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5,1,3,2]\n
# @lcpr case=end

#

