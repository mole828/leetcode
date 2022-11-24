from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res=0
        l=-1
        lst=0
        for i,s in enumerate(nums):
            if s>right:
                l=i
                lst=0
            elif s>=left:
                res+=i-l
                lst=i-l
            else:
                res+=lst
        return res