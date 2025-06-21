#
# @lc app=leetcode id=3085 lang=python3
# @lcpr version=30204
#
# [3085] Minimum Deletions to Make String K-Special
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)
        def f(x: int) -> int:
            f_res = 0
            x_k = x + k
            for v in counter.values():
                if v < x:
                    f_res += v
                elif v > x_k:
                    f_res += v - x_k
            return f_res
        
        right = max(counter.values())
        min_value = float('inf')
        for i in range(right+1):
            min_value = min(min_value, f(i))
        return min_value
    
    def minimumDeletions2(self, word: str, k: int) -> int:
        counter = Counter(word)
        arr = sorted(counter.values())
        res = float('inf')
        for left_i, left_v in enumerate(arr):
            right_v = left_v + k
            temp = sum(arr[:left_i])
            for i, v in enumerate(arr):
                if v > right_v:
                    temp += v - right_v
            res = min(res, temp)
        return res


# @lc code=end



#
# @lcpr case=start
# "aabcaba"\n0\n
# @lcpr case=end

# @lcpr case=start
# "dabdcbdcdcd"\n2\n
# @lcpr case=end

# @lcpr case=start
# "aaabaaa"\n2\n
# @lcpr case=end

#

