package problems.p3742
/*
 * @lc app=leetcode id=3742 lang=kotlin
 *
 * [3742] Maximum Path Score in a Grid
 */

// @lc code=start
class Solution {
    fun maxPathScore(grid: Array<IntArray>, k: Int): Int {
        val n = grid.size
        val m = grid[0].size
        val NEG = -1_000_000_000
        val cache = Array(n) { Array(m) { IntArray(k + 1) { Int.MIN_VALUE } } }

        fun dfs(row: Int, col: Int, remainingK: Int): Int {
            if (row < 0 || col < 0 || remainingK < 0) return NEG
            if (row == 0 && col == 0) return 0
            if (cache[row][col][remainingK] != Int.MIN_VALUE) return cache[row][col][remainingK]

            val gridValue = grid[row][col]
            val nextK = remainingK - if (gridValue > 0) 1 else 0
            val up = dfs(row - 1, col, nextK)
            val left = dfs(row, col - 1, nextK)
            val ans = gridValue + maxOf(up, left)
            cache[row][col][remainingK] = ans
            return ans
        }

        val ans = dfs(n - 1, m - 1, k)
        return if (ans < 0) -1 else ans
    }
}
// @lc code=end
