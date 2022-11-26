from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        return ','.join([str(i) for i in sorted(nums)]) in ','.join([str(i) for i in nums*2])


if __name__ == '__main__':
    Solution().check([1,2,3,4,5])