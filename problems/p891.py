from typing import List


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        sons = []
        def dfs(stack: List[int], index:int):
            if index == len(nums):
                sons.append(stack)
                return
            dfs(stack+[nums[index]], index+1)
            dfs(stack, index+1)
        dfs([],0)
        widths = [ max(son)-min(son) for son in sons if son ]
        MOD = 10**9+7
        return sum(widths)%MOD

class Solution(object):
    def sumSubseqWidths(self, nums: List[int]):
        nums.sort()
        sums=0
        for i in range(len(nums)):
            sums=sums+(pow(2,i,1000000007)-pow(2,len(nums)-1-i,1000000007))*nums[i]
        return sums%1000000007

if __name__ == '__main__':
    Solution().sumSubseqWidths([2,1,3])