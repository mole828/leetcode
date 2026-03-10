package leetcode.problems._3130
/*
 * @lc app=leetcode id=3130 lang=kotlin
 *
 * [3130] Find All Possible Stable Binary Arrays II
 */
// @lc code=start
// 通用记忆化封装：接受一个 (K) -> V 的函数，返回一个带缓存的 (K) -> V
class Solution {
    fun numberOfStableArrays(zero: Int, one: Int, limit: Int): Int {
        val MOD = 1_000_000_007L
        // 使用三维数组进行记忆化：dp[i][j][k]
        val memo = Array(zero + 1) { Array(one + 1) { LongArray(2) { -1L } } }

        fun dfs(i: Int, j: Int, k: Int): Long {
            if (i == 0) return if (k == 1 && j <= limit) 1L else 0L
            if (j == 0) return if (k == 0 && i <= limit) 1L else 0L
            if (memo[i][j][k] != -1L) return memo[i][j][k]

            val res = when (k) {
                0 -> { // 当前填 0
                    val count = (dfs(i - 1, j, 0) + dfs(i - 1, j, 1))
                    val offset = if (i > limit) dfs(i - limit - 1, j, 1) else 0L
                    (count - offset + MOD) % MOD
                }
                else -> { // 当前填 1
                    val count = (dfs(i, j - 1, 0) + dfs(i, j - 1, 1))
                    val offset = if (j > limit) dfs(i, j - limit - 1, 0) else 0L
                    (count - offset + MOD) % MOD
                }
            }
            
            return res.also { memo[i][j][k] = it }
        }

        return ((dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD).toInt()
    }
}
// @lc code=end

