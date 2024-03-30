#
# @lc app=leetcode id=992 lang=python3
# @lcpr version=
#
# [992] Subarrays with K Different Integers
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    # Time Limit Exceeded, 40/55 cases passed
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = 0
        for left in range(len(nums)):
            for right in range(left, len(nums)):
                sub = nums[left:right+1]
                if len(set(sub)) == k:
                    # print(sub)
                    count += 1
        return count
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cnt=[0]*(len(nums)+1)
        ans=0
        l=0
        left=0
        for num in nums: # num is right
            print(cnt)
            cnt[num]+=1
            if cnt[num]==1:
                k-=1
                if k<0:
                    cnt[nums[left]]=0
                    left+=1
                    l=left
            if k<=0:
                while cnt[nums[left]]>1:
                    cnt[nums[left]]-=1
                    left+=1
                ans+=left-l+1
        return ans                        
# @lc code=end

print(Solution().subarraysWithKDistinct([1,2,1,2,3],2))

#
# @lcpr case=start
# [1,2,1,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,3,4]\n3\n
# @lcpr case=end

#

