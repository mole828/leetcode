#
# @lc app=leetcode id=1092 lang=python3
#
# [1092] Shortest Common Supersequence 
#

# @lc code=start
# link: https://leetcode.cn/problems/shortest-common-supersequence/solutions/2194615/cong-di-gui-dao-di-tui-jiao-ni-yi-bu-bu-auy8z/
# 会超时的递归代码
from functools import cache


class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        if s == "": return t  # s 是空串，返回剩余的 t
        if t == "": return s  # t 是空串，返回剩余的 s
        if s[-1] == t[-1]:  # 最短公共超序列一定包含 s[-1]
            return self.shortestCommonSupersequence(s[:-1], t[:-1]) + s[-1]
        ans1 = self.shortestCommonSupersequence(s[:-1], t)
        ans2 = self.shortestCommonSupersequence(s, t[:-1])
        if len(ans1) < len(ans2):  # 取 ans1 和 ans2 中更短的组成答案
            return ans1 + s[-1]
        return ans2 + t[-1]
        

# 能通过的测试数据更多，但仍然超时（超内存），还需要进一步优化
class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        # dfs(i,j) 返回 s 的前 i 个字母和 t 的前 j 个字母的最短公共超序列
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, j: int) -> str:
            if i < 0: return t[:j + 1]  # s 是空串，返回剩余的 t
            if j < 0: return s[:i + 1]  # t 是空串，返回剩余的 s
            if s[i] == t[j]:  # 最短公共超序列一定包含 s[i]
                return dfs(i - 1, j - 1) + s[i]
            ans1 = dfs(i - 1, j)
            ans2 = dfs(i, j - 1)
            if len(ans1) < len(ans2):  # 取 ans1 和 ans2 中更短的组成答案
                return ans1 + s[i]
            return ans2 + t[j]
        return dfs(len(s) - 1, len(t) - 1)

class Solution:
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        # dfs(i,j) 返回 s 的前 i 个字母和 t 的前 j 个字母的最短公共超序列的长度
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, j: int) -> int:
            if i < 0: return j + 1  # s 是空串，返回剩余的 t 的长度
            if j < 0: return i + 1  # t 是空串，返回剩余的 s 的长度
            if s[i] == t[j]:  # 最短公共超序列一定包含 s[i]
                return dfs(i - 1, j - 1) + 1
            return min(dfs(i - 1, j), dfs(i, j - 1)) + 1

        # make_ans(i,j) 返回 s 的前 i 个字母和 t 的前 j 个字母的最短公共超序列
        # 看上去和 dfs 没啥区别，但是末尾的递归是 if-else
        # make_ans(i-1,j) 和 make_ans(i,j-1) 不会都调用
        # 所以 make_ans 的递归树仅仅是一条链
        def make_ans(i: int, j: int) -> str:
            if i < 0: return t[:j + 1]  # s 是空串，返回剩余的 t
            if j < 0: return s[:i + 1]  # t 是空串，返回剩余的 s
            if s[i] == t[j]:  # 公共超序列一定包含 s[i]
                return make_ans(i - 1, j - 1) + s[i]
            # 如果下面 if 成立，说明上面 dfs 中的 min 取的是 dfs(i - 1, j)
            # 说明 dfs(i - 1, j) 对应的公共超序列更短
            # 那么就在 make_ans(i - 1, j) 的结果后面加上 s[i]
            # 否则说明 dfs(i, j - 1) 对应的公共超序列更短
            # 那么就在 make_ans(i, j - 1) 的结果后面加上 t[j]
            if dfs(i, j) == dfs(i - 1, j) + 1:
                return make_ans(i - 1, j) + s[i]
            return make_ans(i, j - 1) + t[j]

        return make_ans(len(s) - 1, len(t) - 1)
# @lc code=end

print(Solution().shortestCommonSupersequence("abac", "cab")) # "cabac"