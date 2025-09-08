#
# @lc app=leetcode id=3495 lang=python3
# @lcpr version=30204
#
# [3495] Minimum Operations to Make Array Elements Zero
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from bisect import bisect_left, bisect_right
from math import ceil
from typing import List


class Solution:
    # timeout
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for left, right in queries:
            ans += ceil(sum(ceil(num.bit_length()/2) for num in range(left, right + 1)) / 2)
        return ans
    
pre = [1]
tmp = 1
while tmp <= 10**9:
    tmp *= 4
    pre.append(tmp)

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        ans = 0
        for left, right in queries:
            index_left, index_right = bisect_left(pre, left), bisect_right(pre, right)
            tmp = 0
            last = left
            for i in range(index_left, index_right):
                tmp += (pre[i] - last) * i
                last = pre[i]
            tmp += (right - last + 1) * index_right
            ans += ceil(tmp/2)
        return ans
# @lc code=end

print(Solution().minOperations([[1,2], [2,4]]))

#
# @lcpr case=start
# [[1,2],[2,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,6]]\n
# @lcpr case=end

#

