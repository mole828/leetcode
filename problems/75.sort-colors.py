#
# @lc app=leetcode id=75 lang=python3
# @lcpr version=
#
# [75] Sort Colors
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0, c1, c2 = 0, 0, 0
        for x in nums:
            if x == 0:
                c0 += 1
            elif x == 1:
                c1 += 1
            else:
                c2 += 1
        i = 0
        for _ in range(c0):
            nums[i] = 0
            i += 1
        for _ in range(c1):
            nums[i] = 1
            i += 1
        for _ in range(c2):
            nums[i] = 2
            i += 1

# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#

