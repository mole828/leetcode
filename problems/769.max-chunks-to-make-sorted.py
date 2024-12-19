#
# @lc app=leetcode id=769 lang=python3
# @lcpr version=
#
# [769] Max Chunks To Make Sorted
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        target = sorted(arr)
        ans = 0
        cur = 0
        for i in range(len(arr)):
            cur = max(cur, arr[i])
            if cur == target[i]:
                ans += 1
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [4,3,2,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,2,3,4]\n
# @lcpr case=end

#

