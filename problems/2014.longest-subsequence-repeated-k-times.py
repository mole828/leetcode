#
# @lc app=leetcode id=2014 lang=python3
#
# [2014] Longest Subsequence Repeated k Times
#

# @lc code=start
from collections import Counter
from itertools import permutations


class Solution:
    # 392. 判断子序列
    # 返回 seq 是否为 s 的子序列
    def isSubsequence(self, seq: str, s: str) -> bool:
        it = iter(s)
        return all(c in it for c in seq)  # in 会消耗迭代器

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cnt = Counter(s)
        a = [ch for ch, freq in cnt.items() for _ in range(freq // k)]
        a.sort(reverse=True)

        for i in range(len(a), 0, -1):
            for perm in permutations(a, i):  # a 的长为 i 的排列
                seq = ''.join(perm)
                if self.isSubsequence(seq * k, s):  # seq*k 是 s 的子序列
                    return seq
        return ''

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/longest-subsequence-repeated-k-times/solutions/1006067/mei-ju-pai-lie-zi-xu-lie-pi-pei-by-endle-oi2h/
# @lc code=end

print(Solution().longestSubsequenceRepeatedK(s = "letsleetcode", k = 2))