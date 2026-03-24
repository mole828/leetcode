package problems.p2906
/*
 * @lc app=leetcode id=2906 lang=kotlin
 *
 * [2906] Construct Product Matrix
 */

// @lc code=start
const val MOD = 12345
class Solution {
    fun constructProductMatrix(grid: Array<IntArray>): Array<IntArray> {
        val n = grid.size
        val m = grid[0].size
        val p = Array(n) { IntArray(m) }

        // 1. 计算后缀积并存入结果矩阵
        var suf = 1
        for (i in n - 1 downTo 0) {
            for (j in m - 1 downTo 0) {
                p[i][j] = suf
                // 注意：Kotlin 中 Long 转型处理防止溢出，虽然 12345^2 不会溢出 Int
                suf = (suf.toLong() * grid[i][j] % MOD).toInt()
            }
        }

        // 2. 计算前缀积并与原结果相乘
        var pre = 1
        for (i in 0 until n) {
            for (j in 0 until m) {
                p[i][j] = (p[i][j].toLong() * pre % MOD).toInt()
                pre = (pre.toLong() * grid[i][j] % MOD).toInt()
            }
        }

        return p
    }
}
// @lc code=end

