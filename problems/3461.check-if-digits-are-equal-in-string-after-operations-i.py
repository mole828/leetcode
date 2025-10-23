#
# @lc app=leetcode id=3461 lang=python3
#
# [3461] Check If Digits Are Equal in String After Operations I
#

# @lc code=start
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) == 2:
            return s[0] == s[1]
        nums = [int(c) for c in s]
        next_num = [(nums[i]+nums[i+1])%10 for i in range(len(nums)-1)]
        return self.hasSameDigits(''.join(map(str, next_num)))
# @lc code=end

