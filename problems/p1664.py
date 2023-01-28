from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        predx = 0
        lastdx = sum(nums[i] * (-1)**i for i in range(len(nums)))
        ans = 0
        for num in nums:
            lastdx = -lastdx + num
            if lastdx == predx:ans+=1
            predx = -predx + num
        return ans

if __name__ == '__main__':
    Solution().waysToMakeFair(nums = [2,1,6,4])