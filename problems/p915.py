
from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        split = 0
        left_max = nums[0]
        all_max = nums[0]
        for i in range(1,len(nums)):
            if nums[i] >= left_max:
                all_max = max(all_max, nums[i])
            else:
                split = i
                left_max = all_max
        return split + 1

if __name__ == '__main__':
    sol = Solution()
    for data in [
        [5,0,3,8,6], # 3
        [1,1,1,0,6,12], # 4
        [1,1], # 1
    ]:
        print(data, '=>', sol.partitionDisjoint(data))