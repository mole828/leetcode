#
# @lc app=leetcode id=2108 lang=python3
#
# [2108] Find First Palindromic String in the Array
#

# @lc code=start
from typing import List

def isPalindromic(word: str) -> bool :
    for i in range(len(word)//2):
        if word[i]!=word[-i-1]:
            return False
    return True

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if isPalindromic(word):
                return word 
        return ""
# @lc code=end

