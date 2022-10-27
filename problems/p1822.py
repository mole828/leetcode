from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c=0
        for num in nums:
            if num==0:return 0
            if num<0:c+=1
        return (-1)**c


if __name__ == '__main__':
    print(Solution().arraySign([-1,1,-1,1,-1]))