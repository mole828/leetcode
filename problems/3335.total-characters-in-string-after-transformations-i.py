#
# @lc app=leetcode id=3335 lang=python3
#
# [3335] Total Characters in String After Transformations I
#

# @lc code=start
from collections import Counter


class Solution:
    def nextChar(s: str) -> str:
        if s == 'z':
            return 'ab'
        return chr(ord(s) + 1)
    MOD = 1_000_000_007
    # Time Limit Exceeded, 802/824 cases passed
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        c = Counter(s)
        while t > 0:
            newCount = Counter()
            for k, v in c.items():
                for c in Solution.nextChar(k):
                    newCount[c] += v % Solution.MOD
            t -= 1
            c = newCount
        return sum(newCount.values()) % Solution.MOD
    
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        arr = [0] * 26
        ord_a = ord('a')
        for c in s:
            arr[ord(c) - ord_a] += 1
        for i in range(t):
            new_arr = [0] * 26
            for j in range(26):
                new_arr[j] = arr[j - 1]
            new_arr[1] += arr[-1] 
            arr = new_arr
        return sum(arr) % Solution.MOD
        
# @lc code=end

print(Solution().lengthAfterTransformations('abcyy', 2))