#
# @lc app=leetcode id=3129 lang=python3
#
# [3129] Find All Possible Stable Binary Arrays I
#

# @lc code=start
from functools import cache


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(
                last_zero: int, 
                last_one: int, 
                continue_zero: int, 
                continue_one: int
            ) -> int:
            # print(f"dfs({last_zero}, {last_one}, {continue_zero}, {continue_one})")
            if continue_zero > limit or continue_one > limit:
                return 0
            if last_zero == 0 and last_one == 0:
                return 1
            _sum = 0
            if last_zero:
                _sum += dfs(
                    last_zero=last_zero-1,
                    last_one=last_one,
                    continue_zero=continue_zero+1,
                    continue_one=0,
                )
            if last_one:
                _sum += dfs(
                    last_zero=last_zero,
                    last_one=last_one-1,
                    continue_zero=0,
                    continue_one=continue_one+1,
                )
            # print(f"dfs({last_zero}, {last_one}, {continue_zero}, {continue_one}) = {_sum}")
            return _sum % MOD
        return dfs(zero, one, 0, 0)
    
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 1_000_000_007
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int, k: int) -> int:
            if i == 0:
                return 1 if k == 1 and j <= limit else 0
            if j == 0:
                return 1 if k == 0 and i <= limit else 0
            if k == 0:
                return (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - (dfs(i - limit - 1, j, 1) if i > limit else 0)) % MOD
            else:  # else 可以去掉，这里仅仅是为了代码对齐
                return (dfs(i, j - 1, 0) + dfs(i, j - 1, 1) - (dfs(i, j - limit - 1, 0) if j > limit else 0)) % MOD
        ans = (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD
        dfs.cache_clear()  # 防止爆内存
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-ii/solutions/2758868/dong-tai-gui-hua-cong-ji-yi-hua-sou-suo-37jdi/
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfStableArrays(1, 1, 2))