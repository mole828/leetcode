#
# @lc app=leetcode id=3333 lang=python3
#
# [3333] Find the Original Typed String II
#

# @lc code=start

from itertools import accumulate


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if n < k:  # 无法满足要求
            return 0

        MOD = 1_000_000_007
        cnts = []
        ans = 1
        cnt = 0
        for i in range(n):
            cnt += 1
            if i == n - 1 or word[i] != word[i + 1]:
                # 如果 cnt = 1，这组字符串必选，无需参与计算
                if cnt > 1:
                    if k > 0:
                        cnts.append(cnt - 1)
                    ans = ans * cnt % MOD
                k -= 1  # 注意这里把 k 减小了
                cnt = 0

        if k <= 0:
            return ans

        f = [[0] * k for _ in range(len(cnts) + 1)]
        f[0] = [1] * k
        for i, c in enumerate(cnts):
            # 计算 f[i] 的前缀和数组 s
            s = list(accumulate(f[i], initial=0))
            # 计算子数组和
            for j in range(k):
                f[i + 1][j] = (s[j + 1] - s[max(j - c, 0)]) % MOD
        return (ans - f[-1][-1]) % MOD

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-the-original-typed-string-ii/solutions/2966856/zheng-nan-ze-fan-qian-zhui-he-you-hua-dp-5mi9/
        
# @lc code=end

print(Solution().possibleStringCount("aabbccdd", 7))