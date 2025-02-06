#
# @lc app=leetcode id=1726 lang=python3
# @lcpr version=30204
#
# [1726] Tuple with Same Product
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0
        product_map = {}
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                if product in product_map:
                    product_map[product] += 1
                else:
                    product_map[product] = 1
        res = 0
        for product in product_map:
            count = product_map[product]
            if count > 1:
                res += count * (count - 1) * 4
        return res
        
# @lc code=end



#
# @lcpr case=start
# [2,3,4,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,4,5,10]\n
# @lcpr case=end

#

