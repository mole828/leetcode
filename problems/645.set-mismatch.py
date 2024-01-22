#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# 为什么会有这种题目，
# 不接受 [1,2] 和 [2,1] 相同。

# @lc code=start
class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        v = [0] * (n + 1)
        missing, duplicate = 0, 0

        for num in nums:
            v[num] += 1

        for i in range(1, len(v)):
            if v[i] == 2:
                duplicate = i
            if v[i] == 0:
                missing = i

        return [duplicate, missing]
# @lc code=end

