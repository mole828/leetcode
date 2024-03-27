#
# @lc app=leetcode id=713 lang=python3
# @lcpr version=
#
# [713] Subarray Product Less Than K
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache, reduce
from typing import List



# Time Limit Exceeded, 34/98 cases passed
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        def product(nums: List[int]) -> int:
            return reduce(lambda a,b:a*b, nums)
        count = 0
        for left in range(len(nums)):
            for right in range(left, len(nums)):
                sub = nums[left:right+1]
                if product(sub)<k:
                    count += 1
                # print(sub)
        return count

# Time Limit Exceeded, 35/98 cases passed
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        @cache
        def product2(i: int) -> int:
            if i==-1:
                return 1 
            return nums[i] * product2(i-1)
        for left in range(-1,len(nums)):
            for right in range(left+1, len(nums)):
                sub_product = product2(right)//product2(left)
                if sub_product<k:
                    count+=1
        return count
    
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        nums.append(1)
        count = 0
        data = {
            'left': 0,
            'right': 1,
            'product': nums[0],
        }
        length = len(nums)
        def right_go():
            data['product'] *= nums[data['right']]
            data['right'] += 1
        def left_go():
            data['product'] //= nums[data['left']]
            data['left'] += 1

        while data['right']<length:
            # print({"sub": nums[data['left']:data['right']], 'data':data})
            if data['product']<k:
                count += data['right'] - data['left']
                right_go()
            else:
                left_go()
            if data['left']==data['right']:
                right_go()
            
        return count
# @lc code=end

print(Solution().numSubarrayProductLessThanK([10,5,2,6],100))
print(Solution().numSubarrayProductLessThanK([1,2,3],0))


#
# @lcpr case=start
# [10,5,2,6]\n100\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n0\n
# @lcpr case=end

#

