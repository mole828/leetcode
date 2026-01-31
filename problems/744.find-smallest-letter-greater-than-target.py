#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ord_target = ord(target)
        ord_letters = (ord(c) for c in letters)
        bigger_letters = (c for c in ord_letters if c > ord_target)
        return chr(min(bigger_letters, default=ord(letters[0])))
        
        
# @lc code=end

