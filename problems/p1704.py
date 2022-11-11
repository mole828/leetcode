'''
阅读理解
'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ('a','e','i','o','u','A','E','I','O','U')
        half_len = len(s) // 2
        return sum(i in vowel for i in s[:half_len]) == sum(i in vowel for i in s[half_len:])