#
# @lc app=leetcode id=440 lang=python3
# @lcpr version=
#
# [440] K-th Smallest in Lexicographical Order
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

# link https://leetcode.cn/problems/k-th-smallest-in-lexicographical-order/solutions/1360662/by-ac_oier-m3zl/
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def get_cnt(x: int, limit: int):
            a, b = str(x), str(limit)
            k = len(b) - len(a)
            ans = sum(10 ** i for i in range(k)) if k else 0
            ans += 10 ** k if (u := int(b[:len(a)])) > x else limit - x * 10 ** k + 1 if u == x else 0
            return ans

        ans = 1
        while k > 1:
            ans = ans + 1 if (cnt := get_cnt(ans, n)) < k else ans * 10
            k -= cnt if cnt < k else 1
        return ans
# @lc code=end



#
# @lcpr case=start
# 13\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#

