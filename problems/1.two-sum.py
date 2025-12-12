#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has: Dict[int, int] = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in has:
                return [has[num], i]
            need = target - num
            has[need] = i
        raise ValueError("No two sum solution")


# @lc code=end

if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
