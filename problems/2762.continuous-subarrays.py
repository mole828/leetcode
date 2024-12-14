#
# @lc app=leetcode id=2762 lang=python3
# @lcpr version=30204
#
# [2762] Continuous Subarrays
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque
from typing import List


# 子数组 最大-最小<=2 l==r 双端优先队列 可以先入队 再出队
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        q1 = deque() 
        q2 = deque() 
        ans = l = 0
        for r, x in enumerate(nums):
            while q1 and nums[q1[-1]] <= x:
                q1.pop()
            while q2 and nums[q2[-1]] >= x:
                q2.pop()
            q1.append(r); q2.append(r)
            while nums[q1[0]] - nums[q2[0]] > 2:
                if q1[0] == l: q1.popleft()
                if q2[0] == l: q2.popleft()
                l += 1
            ans += r - l + 1
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [5,4,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

