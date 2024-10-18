#
# @lc app=leetcode id=670 lang=python3
# @lcpr version=
#
# [670] Maximum Swap
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        output = 0
        while nums and nums[0] == max(nums):
            v = nums.pop(0)
            output = output*10 + int(v)
        print(output)
        if nums:
            max_v = max(nums)
            max_i = len(nums)-1
            while nums[max_i] != max_v:
                max_i -= 1
            nums[max_i] = nums[0]
            nums[0] = max_v
        for i in nums:
            output = output*10 + int(i)
        return output

# @lc code=end

print(Solution().maximumSwap(2736))

#
# @lcpr case=start
# 2736\n
# @lcpr case=end

# @lcpr case=start
# 9973\n
# @lcpr case=end

#

