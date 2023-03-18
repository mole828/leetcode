# link: https://leetcode.cn/problems/split-two-strings-to-make-palindrome/solution/mei-xiang-ming-bai-yi-zhang-tu-miao-dong-imvy/

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(a: str, b: str) -> bool:
            i, j = 0, len(a) - 1  
            while i < j and a[i] == b[j]: 
                i += 1
                j -= 1
            s, t = a[i: j + 1], b[i: j + 1] 
            return s == s[::-1] or t == t[::-1]  
        return check(a, b) or check(b, a)
