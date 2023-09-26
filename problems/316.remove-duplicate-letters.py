#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        has = set()
        result = []
        for c in s :
            # print(counter, has, result)
            counter[c] -= 1
            if c in has:
                continue
            while result and\
                c < result[-1] and\
                counter[result[-1]]>0:
                has.remove(result.pop())
            has.add(c)
            result.append(c)

        return ''.join(result)
# @lc code=end

print(Solution().removeDuplicateLetters("bcabc"))