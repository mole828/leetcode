from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ls = [1]*len(nums)
        for i in range(len(ls)):
            for j in range(i):
                if nums[j]<nums[i]:
                    ls[i] = max(ls[i],ls[j]+1)
            print(ls)
        return max(ls)
    
if __name__ == '__main__':
    Solution().lengthOfLIS([10,9,2,5,3,7,101,18])