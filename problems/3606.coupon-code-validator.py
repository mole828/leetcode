#
# @lc app=leetcode id=3606 lang=python3
# @lcpr version=30204
#
# [3606] Coupon Code Validator
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
BUSINESS_LINE_TO_CATEGORY = {
    "electronics": 0,
    "grocery": 1,
    "pharmacy": 2,
    "restaurant": 3,
}

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        groups = [[] for _ in range(len(BUSINESS_LINE_TO_CATEGORY))]
        for s, bus, active in zip(code, businessLine, isActive):
            category = BUSINESS_LINE_TO_CATEGORY.get(bus, -1)
            if s and category >= 0 and active and \
               all(c == '_' or c.isalnum() for c in s):
                groups[category].append(s)  # 相同类别的优惠码分到同一组

        ans = []
        for g in groups:
            g.sort()  # 每一组内部排序
            ans += g
        return ans

# @lc code=end

# print(Solution().validateCoupons(
#     ["SAVE20","","PHARMA5","SAVE@20"],
#     ["restaurant","grocery","pharmacy","restaurant"],
#     [True,True,True,True]
# ))

s_list = ['aba', 'bab']
print(sorted(s_list, key=lambda x:x[::-1])) # ['aba', 'bab']
print(sorted(s_list, reverse=True)) # ['bab', 'aba']

#
# @lcpr case=start
# ["SAVE20","","PHARMA5","SAVE@20"]\n["restaurant","grocery","pharmacy","restaurant"]\n[true,true,true,true]\n
# @lcpr case=end

# @lcpr case=start
# ["GROCERY15","ELECTRONICS_50","DISCOUNT10"]\n["grocery","electronics","invalid"]\n[false,true,true]\n
# @lcpr case=end

#

