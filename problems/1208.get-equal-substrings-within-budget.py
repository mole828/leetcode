#
# @lc app=leetcode id=1208 lang=python3
# @lcpr version=
#
# [1208] Get Equal Substrings Within Budget
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from bisect import bisect


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(a)-ord(b)) for a,b in zip(s,t)]
        cost_sum = [0]
        for cost in costs:
            cost_sum.append(cost_sum[-1]+cost)
        print(cost_sum)
        result = 0
        for i in range(len(cost_sum)):
            v = cost_sum[i]
            target_v = v+maxCost
            j = bisect(cost_sum, target_v) - 1
            result = max(result, j-i)
        return result
# @lc code=end

print(Solution().equalSubstring("abcd", "bcdf", 3))
print(Solution().equalSubstring("abcd", "cdef", 3))

#
# @lcpr case=start
# "abcd"\n"bcdf"\n3\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"cdef"\n3\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n"acde"\n0\n
# @lcpr case=end

#

