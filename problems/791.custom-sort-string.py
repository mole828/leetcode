#
# @lc app=leetcode id=791 lang=python3
# @lcpr version=
#
# [791] Custom Sort String
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        chars = [c for c in s]
        def index(c: str) -> int:
            try:
                return order.index(c)
            except:
                return float('inf')
        chars.sort(key=lambda c:index(c))
        return ''.join(chars)
        
# @lc code=end


print(Solution().customSortString('cba', 'abcd'))
#
# @lcpr case=start
# "cba"\n"abcd"\n
# @lcpr case=end

# @lcpr case=start
# "bcafg"\n"abcd"\n
# @lcpr case=end

#

