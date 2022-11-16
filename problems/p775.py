from typing import List


class Solution:
    def isIdealPermutation(self, nums:List[int]):
        for i in range(len(nums)):
            if abs(nums[i] - i) > 1:
                return False
        return True