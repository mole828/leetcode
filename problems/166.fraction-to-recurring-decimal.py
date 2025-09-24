#
# @lc app=leetcode id=166 lang=python3
# @lcpr version=30204
#
# [166] Fraction to Recurring Decimal
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator*denominator<0 else ''
        numerator, denominator = abs(numerator), abs(denominator)

        p, r = divmod(numerator, denominator)
        ans = [sign + str(p)]
        if r == 0:
            pass
        else:
            ans.append('.')
            mp = {r: len(ans)}
            while r:
                p, r = divmod(r * 10, denominator)
                ans.append(str(p))
                if r in mp:
                    pos = mp[r]
                    return f"{''.join(ans[:pos])}({''.join(ans[pos:])})"
                mp[r] = len(ans)
        return ''.join(ans)

        
# @lc code=end

print(Solution().fractionToDecimal(4, 333))

#
# @lcpr case=start
# 1\n2\n
# @lcpr case=end

# @lcpr case=start
# 2\n1\n
# @lcpr case=end

# @lcpr case=start
# 4\n333\n
# @lcpr case=end

#

