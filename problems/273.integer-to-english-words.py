#
# @lc app=leetcode id=273 lang=python3
# @lcpr version=
#
# [273] Integer to English Words
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution(object):
    def numberToWords(self, num):
        to19 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def words(n):
            if n < 20:
                return to19[n - 1 : n]
            if n < 100:
                return [tens[n // 10 - 2]] + words(n % 10)
            if n < 1000:
                return [to19[n // 100 - 1]] + ['Hundred'] + words(n % 100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000 ** (p + 1):
                    return words(n // 1000 ** p) + [w] + words(n % 1000 ** p)
        
        return ' '.join(words(num)) or 'Zero'
# @lc code=end



#
# @lcpr case=start
# 123\n
# @lcpr case=end

# @lcpr case=start
# 12345\n
# @lcpr case=end

# @lcpr case=start
# 1234567\n
# @lcpr case=end

#

