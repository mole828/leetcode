#
# @lc app=leetcode id=564 lang=python3
# @lcpr version=
#
# [564] Find the Closest Palindrome
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Time Limit Exceeded, 163/217 cases passed (N/A)
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def palind(x: int)->bool:
            s = str(x)
            for i in range(len(s)//2):
                if s[i] != s[-i-1]:
                    return False
            return True
        x = int(n)
        d = 1
        while not palind(x-d) and not palind(x+d):
            d += 1
        if palind(x-d):
            return str(x-d)
        return str(x+d)
    
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length, int_n = len(n), int(n)
        if int_n < 10 or int_n == 10 ** (length-1): return str(int_n-1)
        if int_n - 1 == 10 ** (length-1): return str(int_n-2)
        if int_n + 1 == 10 ** length: return str(int_n + 2)

        pre = int(n[:(length+1)//2])
        tmp = [s[:length//2] + s[::-1] for s in [str(pre + dx) for dx in (-1, 0, 1)]]
        return min(tmp, key=lambda x: (x==n, abs(int(x)-int_n)))

# @lc code=end

print(Solution().nearestPalindromic("123"))
print(Solution().nearestPalindromic("1234"))

#
# @lcpr case=start
# "123"\n
# @lcpr case=end

# @lcpr case=start
# "1"\n
# @lcpr case=end

#

