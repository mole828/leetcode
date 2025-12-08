#
# @lc app=leetcode id=1925 lang=python3
#
# [1925] Count Square Sum Triples
#

# @lc code=start
class Solution:
    def countTriples(self, n: int) -> int:
        squares = set(i * i for i in range(1, n + 1))
        ans_set = set()
        for a in squares:
            for b in squares:
                if a + b in squares:
                    ans_set.add((a, b))
                    ans_set.add((b, a))
        return len(ans_set)
# @lc code=end

