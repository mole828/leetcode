from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) != 1:
            flag = True
            newNums = []
            for i in range(0, len(nums), 2):
                if flag:
                    newNums.append(min(nums[i], nums[i + 1]))
                else:
                    newNums.append(max(nums[i], nums[i + 1]))
                flag = not flag
            nums = newNums
        return nums[0]