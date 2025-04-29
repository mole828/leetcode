#
# @lc app=leetcode id=2962 lang=python3
# @lcpr version=
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    # Time Limit Exceeded, 516/633 cases passed
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0 
        for left in range(len(nums)):
            for right in range(left,len(nums)):
                sub = nums[left:right+1]
                if sub.count(max(nums)) >= k:
                    count += 1 
                    # print(sub)
        return count
    # Time Limit Exceeded, 622/633 cases passed
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0 
        max_num = max(nums) 
        for left in range(len(nums)):
            count_of_max_num = 0 
            for right in range(left, len(nums)):
                if nums[right] == max_num:
                    count_of_max_num += 1 
                if count_of_max_num == k:
                    count += len(nums) - right 
                    break
        return count
    
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        index_max_num = [
            i for i,num in enumerate(nums)
            if num == max_num
        ] 
        if len(index_max_num)<k:
            return 0
        window = [-1] + [
            index_max_num.pop(0) 
            for _ in range(k-1)
        ]
        count = 0
        while index_max_num: 
            window.append(index_max_num.pop(0))
            # print(window)
            count += (window[1]-window[0])*(len(nums)-window[-1])
            window.pop(0)
        return count
        
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        ans = cnt_mx = left = 0
        for x in nums:
            if x == mx:
                cnt_mx += 1
            while cnt_mx == k:
                if nums[left] == mx:
                    cnt_mx -= 1
                left += 1
            ans += left
        return ans

# @lc code=end

print(Solution().countSubarrays([1,3,2,3,3], 2))
print(Solution().countSubarrays([
    61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82
], 2))

#
# @lcpr case=start
# [1,3,2,3,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,4,2,1]\n3\n
# @lcpr case=end

#

